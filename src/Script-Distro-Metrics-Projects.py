import requests
import csv
import datetime

#ADD YOUR CREDENTIALS TO CONTRIBUTE
credentials = [
    {'user': 'TestSmell', 'token': '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'},
    {'user': 'Flaky', 'token': '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'}
    ]

username = credentials[0]['user']
token = credentials[0]['token']

countSession = 0 #session indice on variable credentials
countRequest = 0 #init request count per repository
countCommits = 0 #init commit count per repository

def changeToken():
    global credentials, countSession, countRequest, username, token
    if(countSession >= (len(credentials)-1)):
        countSession = 0
    else:
        countSession = countSession + 1
    username= credentials[countSession]['user']
    token= credentials[countSession]['token']
    countRequest = 0
    
# create a re-usable session object with the user creds in-built
gh_session = requests.Session()
gh_session.auth = (username, token)

dates = []
ncomments = []
count = 0

# add flaky and/or non-flaky sheet path
with open('IssuesNonFlaky.csv') as f:
    for line in f:
        count = count+1
        url = line
        url = url.replace('https://github.com', 'https://api.github.com/repos')
        url = url.replace(url[-1], "")
        print(url)
        results = requests.get(url, headers={'Authorization': 'token '+token})
        countRequest = countRequest+1
        result = results.json()

        if(results.status_code == 200):
            if result['created_at'] is None or result['closed_at'] is None:
                dates.append('N/D')
                ncomments.append('N/D')
            else:
                create_at = result['created_at']
                crt_year = result['created_at'][0] + result['created_at'][1] + result['created_at'][2] + result['created_at'][3]
                crt_mount = result['created_at'][5] + result['created_at'][6]
                crt_day = result['created_at'][8] + result['created_at'][9]      
                d1 = datetime.date(int(crt_year),int(crt_mount),int(crt_day))
                
                closed_at = result['closed_at']
                cls_year = result['closed_at'][0] + result['closed_at'][1] + result['closed_at'][2] + result['closed_at'][3]
                cls_mount = result['closed_at'][5] + result['closed_at'][6]
                cls_day = result['closed_at'][8] + result['closed_at'][9]
                d2 = datetime.date(int(cls_year),int(cls_mount),int(cls_day))
                time_elapsed = d1 - d2
                
                dates.append(time_elapsed.days)
                ncomments.append(result['comments'])

            #print(dates,ncomments)
            if (countRequest == 100 or countRequest == 300 or countRequest == 500 or countRequest == 800 or countRequest == 930):
                print('PRE-PRINT')
                print(dates,ncomments)
            #checks if request is close 1000
            if (countRequest > 950):
                changeToken()
        else:
            dates.append("N/A")
            ncomments.append("N/A")
f.close()
print(dates,ncomments)