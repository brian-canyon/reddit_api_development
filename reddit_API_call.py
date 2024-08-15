import requests
import urllib3
import time
urllib3.disable_warnings() ## Having trouble with SSL, below code not suited for production

## Creating a connection to Reddit
## The code below is meant to obfuscate the login credentials
## variables: personal_use_script, secret, username, password
def get_login_credentials():
    login_creds = open("C:\\Users\\630227\\Documents\\redditlogin.txt","r")
    login_dict = {}
    for item in login_creds.readlines():
        login_dict[item.split(" ")[0]] = item.split("'")[1]        
    login_creds.close()
    return login_dict      

## Below creates our connection to the reddit API, essentially by passing through the login creds saved above and by using the
## 'requests' library.
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
##requests.get('https://oauth.reddit.com/api/v1/me', headers=headers, verify = False)

## Lastly, we will test our connection by checking to ensure we recieved the correct response code from the reddit API. This
## step will come in handy when we need to verify our pipeline is running correctly. In future itterations of ETL processes,
## we could append these response codes/print statements to a list to have fired off on a daily schedule, that way, if anything
## breaks it would be generally easiser to track down the error. See second print statement.

##if res.status_code == 200:
##    print('Connection Sucsessful!')
##else:
##    print(res)

## Pulling data from posts
## Target is to create table [subreddit, post_title, upvotes, timestamp]
## Table should be sufficient to run a simple regression based analysis as a proof of concept
def top_daily_posts(subreddit):
    url = f"https://oauth.reddit.com/r/{subreddit}/hot"
    try:
        response = requests.get(url, headers=get_reddit_token(), verify= False)
        for post in response.json()['data']['children']:
            print(post['data']['title'])
            print(post['data']['ups'])
    except requests.RequestException as e:
        print(f"Error fetching data from Reddit: {e}")


for i in range(1,10):
    top_daily_posts("News")
    time.sleep(5)


