# My Twitter routines
from authenticating import readconf
import tweepy

keys = readconf()
auth = tweepy.OAuthHandler(keys[0], keys[1])
auth.set_access_token(keys[2], keys[3])
api = tweepy.API(auth)


def tweet_man():  # Manual Input Tweets
    text = str(input("Input tweet: "))
    api.update_status(text)


def tweet_semiman(text):
    api.update_status(text)


def direct_message_man():
    username = str(input("To User: "))
    message = str(input("Message: "))
    api.send_direct_message(user=username, text=message)


def direct_message_semiman(username, message):
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


def tweet_picture_man():
    text = str(input("Input tweet: "))
    image = str(input("Input full path to image: "))
    api.update_with_media(image, text)


def tweet_picture_semiman(image, text):
    api.update_with_media(image, text)
