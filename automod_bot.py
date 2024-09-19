import requests
import urllib3
import json
urllib3.disable_warnings() ## Having trouble with SSL, below code not suited for production

def get_login_credentials():
    login_creds = open("C:\\Users\\630227\\Documents\\redditlogin.txt","r")
    login_dict = {}
    for item in login_creds.readlines():
        login_dict[item.split(" ")[0]] = item.split("'")[1]        
    login_creds.close()
    return login_dict      


def get_reddit_token():
    login_dict = get_login_credentials()
    auth = requests.auth.HTTPBasicAuth(login_dict['personal_use_script'], login_dict['secret'])
    data = {'grant_type': 'password',
            'username': login_dict['username'],
            'password': login_dict['password']}

    headers = {'User-Agent': 'MyBot/0.0.1'}

    res = requests.post('https://www.reddit.com/api/v1/access_token',
                        auth=auth, data=data, headers=headers, verify = False)

    TOKEN = res.json()['access_token']
    headers = {**headers, **{'Authorization': f"bearer {TOKEN}"}}

    return headers

## Creating a function to pull all comments from a speicific sub, in the last 24 hours
subreddit = "AloYoga"
token = get_reddit_token()

post_url = f"https://oauth.reddit.com/r/{subreddit}/new"
response = requests.get(post_url, headers=token, verify= False)
post_id_list = []
post_name_list = []
for post in response.json()['data']['children']:
    post_id_list.append(post['data']['permalink'])
    post_name_list.append(post['data']['title'])
for (id, name) in zip(post_id_list, post_name_list):
    url=f"https://oauth.reddit.com{id}"
    response = requests.get(url, headers=token, verify= False)
    for post in response.json()[1]['data']['children']:
        try:
            #print(post['data']['author'])
            #print(post['data']['body'])
            #print(name)
            print(post)
        except:
            print("keyerror")