import tweepy
from create_login_cfg import create

try:
    # int("hallo")
    f = open("login.cfg", "r")
    consumer_key = f.readline().split(" ")[-1].replace("\n", "")
    consumer_secret = f.readline().split(" ")[-1].replace("\n", "")
    access_token = f.readline().split(" ")[-1].replace("\n", "")
    access_token_secret = f.readline().split(" ")[-1].replace("\n", "")
except:
    print("Login not configured yet.")
    create()

# auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
# auth.set_access_token(access_token, access_token_secret)
#
# api = tweepy.API(auth)
#
# public_tweets = api.home_timeline()
# for tweet in public_tweets:
#     print tweet.text