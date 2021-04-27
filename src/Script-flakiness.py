import requests
import json
import csv

# credentials (please, don't share)
username = ' '
token = ' '

# create a re-usable session object with the user creds in-built
gh_session = requests.Session()
gh_session.auth = (username, token)

languages=["go", "python", "java", "js"]
search_str="flaky AND test"
label_str="bug"
state_str="closed"
# Sorts the results of your query by the number of comments, reactions, reactions-+1, reactions--1, reactions-smile, reactions-thinking_face, reactions-heart, reactions-tada, or interactions. You can also sort results by how recently the items were created or updated, Default: best match
sort_str="created"

# Determines whether the first search result returned is the highest number of matches (desc) or lowest number of matches (asc). This parameter is ignored unless you provide sort. Default: desc
order_str="asc"
pagesize_str="100"
# print(result)
numpages=3
for language_str in languages:
    print("------- {language} -------".format(language=language_str))
    with open('analise.csv', 'a', newline='') as file:
        writer = csv.writer(file)                                                                      
        fieldnames = ["URL"]
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        #writer.writeheader()
        writer.writerow({"URL": language_str})
    for i in range(1, numpages+1):
        print(" Â page {} of {}".format(i, numpages))

        # request a new page

        repos_url='https://api.github.com/search/issues?q={query}+label:{label}+language:{language}+state:{state}&sort={sort}&order={order}&page={numpages}&per_page={pagesize}'.format(query=search_str,label=label_str,language=language_str,state=state_str,sort=sort_str,order=order_str,numpages=str(i),pagesize=pagesize_str)

        # parse text in a json tree (object graph)
        result = json.loads(gh_session.get(repos_url).text)                

        for item in result['items']:                        
            print(item['html_url'])
            with open('analise.csv', 'a', newline='') as file:
                writer = csv.writer(file)                                                                      
                fieldnames = ["URL"]
                writer = csv.DictWriter(file, fieldnames=fieldnames)
                #writer.writeheader()                
                writer.writerow({"URL": item["html_url"]})                   
