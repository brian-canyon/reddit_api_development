import requests
import urllib3
import time
import pandas as pd
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

def top_daily_posts(subreddit, token):
    url = f"https://oauth.reddit.com/r/{subreddit}/hot"
    post_info_df = pd.DataFrame(columns=['subreddit', 'post_title', 'upvote_count', 'upvote_ratio'])
    index = len(post_info_df) + 1
    try:
        response = requests.get(url, headers=token, verify= False)
        for post in response.json()['data']['children']:
            post_info_df = pd.concat([pd.DataFrame([[subreddit, post['data']['title'], post['data']['ups'], post['data']['upvote_ratio']]],
                                                    columns= post_info_df.columns), post_info_df], ignore_index= True)

    except requests.RequestException as e:
        print(f"Error fetching data from Reddit: {e}")
    return post_info_df

def main():
    token = get_reddit_token()
    for i in range(1,10):
        print(top_daily_posts("News", token))
        time.sleep(5)
main()



