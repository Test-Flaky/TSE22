import requests
import json
import csv

#ADD YOUR CREDENTIALS TO CONTRIBUTE
credentials = [
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

languages=["C","Go","Python","Java","JavaScript"]
search_str="test"
label_str="bug"
state_str="closed"
# Sorts the results of your query by the number of comments, reactions, reactions-+1, reactions--1, reactions-smile, reactions-thinking_face, reactions-heart, reactions-tada, or interactions. You can also sort results by how recently the items were created or updated, Default: best match
sort_str="created"

# Determines whether the first search result returned is the highest number of matches (desc) or lowest number of matches (asc). This parameter is ignored unless you provide sort. Default: desc
order_str="asc"
pagesize_str="100"
# print(result)
numpages=10
for language_str in languages:
    print("------- {language} -------".format(language=language_str))
    with open('IssuesNonFlaky.csv', 'a', newline='') as file:
        writer = csv.writer(file)                                                                      
        fieldnames = ["URL"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        #writer.writeheader()
        writer.writerow({"URL": language_str})
    for i in range(1, numpages+1):
        print(" Â page {} of {}".format(i, numpages))

        #checks if request is close 1000
        if (countRequest > 950):
            changeToken()

        # request a new page
        repos_url='https://api.github.com/search/issues?q={query}+label:{label}+language:{language}+state:{state}+is:issue&order={order}&page={numpages}&per_page={pagesize}'.format(query=search_str,label=label_str,language=language_str,state=state_str,order=order_str,numpages=str(i),pagesize=pagesize_str)
        countRequest = countRequest+1
        print(repos_url)

        #  parse text in a json tree (object graph)
        result = json.loads(gh_session.get(repos_url).text)                

        for item in result['items']:                        
            print(item['html_url'])
            with open('IssuesNonFlaky.csv', 'a', newline='') as file:
                writer = csv.writer(file)                                                                      
                fieldnames = ["URL"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                #writer.writeheader()                
                writer.writerow({"URL": item["html_url"]})                   