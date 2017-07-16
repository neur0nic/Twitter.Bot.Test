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


def tweet_semiman(text):
    api.update_status(text)


def direct_message_man():
    username = str(input("To User: "))
    message = str(input("Message: "))
    api.send_direct_message(user=username, text=message)


def direct_message_semiman(username, message)
    api.send_direct_message(user=username, text=message)


def my_follower():
    users = api.followers()
    followers = []
    for i in users:
        followers.append(i.screen_name)
    return followers


def timeline():
    public_tweets = api.home_timeline()
    for tweet in public_tweets:
        print(tweet.user.name + ": " + tweet.text)


def get_dms():
    msgs = api.direct_messages()
    for i in msgs:
        print(i.sender.screen_name + " wrote at " + str(i.created_at) + ": " + i.text + "\n ----------")

# try:
#     follower = ""
#     for i in my_follower():
#         follower += str(i) + ", "
#     text = ("My followers are " + follower)
#     tweet_semiman(text)
# except:
#     print("Error!\n")

# exit()