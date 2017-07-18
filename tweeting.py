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


def tweet_semiman(text):  # expects string
    api.update_status(text)


def direct_message_man():
    username = str(input("To User: "))
    message = str(input("Message: "))
    api.send_direct_message(user=username, text=message)


def direct_message_semiman(username, message):  # expects 2 strings
    api.send_direct_message(user=username, text=message)


def tweet_picture_man():
    text = str(input("Input tweet: "))
    image = str(input("Input full path to image: "))
    api.update_with_media(image, text)


def tweet_picture_semiman(image, text):  # Expects path to file and string
    api.update_with_media(image, text)


def my_follower():
    users = api.followers()
    followers = []
    for i in users:
        followers.append(i.screen_name)
    return followers


def timeline():
    public_tweets = api.home_timeline()
    tweets = []
    for tweet in public_tweets:
        # print(tweet.user.name + ": " + tweet.text)
        tweets.append([tweet.user.screen_name, tweet.text, tweet.id])
    return tweets


def get_dms():
    msgs = api.direct_messages()
    for i in msgs:
        print(i.sender.screen_name + " wrote at " + str(i.created_at) + ": " + i.text + "\n ----------")


def retweet_follower():
    names = my_follower()
    tweets = timeline()
    for i in tweets:
        if i[0] in names:
            api.retweet(i[2])
        else:
            pass


def retweet_by_filter(filter):  # expects list
    tweets = timeline()
    for i in tweets:
        for j in filter:
            if j in i[1]:
                api.retweet(i[2])
            else:
                pass
