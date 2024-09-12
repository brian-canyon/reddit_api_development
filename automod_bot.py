import requests
import urllib3
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
subreddit = "News"
url = f"https://oauth.reddit.com/r/news/comments/1fedyg4/consumer_inflation_slows_to_lowest_rate_since"
token = get_reddit_token()
response = requests.get(url, headers=token, verify= False)
counter = 0
if response.status_code == 200:
    for i in response.json()[1]['data']['children']:
        print(type(i))
        counter = counter + 1
    
    #print(len(response.json()[1]['data']['children']))
else:
    print(response.status_code)

print(counter)