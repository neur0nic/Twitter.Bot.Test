import tweepy, time, sys
from create_login_cfg import create
# import tweeting as t

try:
    # int("hallo")
    f = open("login_sec.cfg", "r")  # muss "login.cfg" heissen
    consumer_key = f.readline().split(" ")[-1].replace("\n", "")
    consumer_secret = f.readline().split(" ")[-1].replace("\n", "")
    access_token = f.readline().split(" ")[-1].replace("\n", "")
    access_token_secret = f.readline().split(" ")[-1].replace("\n", "")
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)
    # print("Success!\n")
except:
    print("Login not configured yet.")
    create()


def tweet_man():  # Manual Input Tweets
    text = str(input("Input tweet: "))
    api.update_status(text)


def direct_message_man():
    username = str(input("To User: "))
    message = str(input("Message: "))
    api.send_direct_message(user=username, text=message)


def my_follower():
    users = api.followers()
    followers = []
    for i in users:
        followers.append(i.screen_name)
    # print(followers)


def timeline():
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.user.name + ": " + tweet.text)


def get_dms():
    
try:
    timeline()
except:
    print("Error!\n")

exit()
