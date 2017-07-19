# My Twitter routines
from authenticating import readconf
import tweepy
from random import randint
import time

keys = readconf()
auth = tweepy.OAuthHandler(keys[0], keys[1])
auth.set_access_token(keys[2], keys[3])
api = tweepy.API(auth)


def bot_off():
    # color = "b22222"
    # api.update_profile_colors(profile_background_color=color)
    api.update_profile(description="I am a Bot programmed in #tweepy..... The Bot is not in 😴")


def bot_on():
    # color = "1da1f2"
    # api.update_profile_colors(profile_background_color=color)
    api.update_profile(description="I am a Bot programmed in #tweepy..... The Bot is in 😀")


def tweet_man():  # Manual Input Tweets
    text = str(input("Input tweet: "))
    api.update_status(text)


def tweet_semiman(text):  # expects string
    api.update_status(text)


def reply_semiman(text, tweetid):  # expects string and integer
    api.update_status(text, in_reply_to_status_id=tweetid)


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


def expect_command():
    tweets = timeline()
    for i in tweets:
        if check_if_done(i):
            pass
        if not check_if_done(i):
            exec_command(i)


def exec_command(tweet):  # Expects single tweet (list)
    commands = ["tell me a joke", "tell me the time"]
    if commands[0] in tweet[2]:
        tell_joke(tweet)
        mark_tweet_done(tweet)
    elif commands[1] in tweet[2]:
        tell_time(tweet)
        mark_tweet_done(tweet)
    # elif commands[2] in i[2]:
    else:
        pass


def check_if_done(tweet):  # Expects single tweet (list)
    f = open("answered.txt", "r")
    answeredtweets = f.readlines()
    f.close()
    if len(answeredtweets) > 50:
        for i in range(0, 25):
            del answeredtweets[0]
    for i in range(0, len(answeredtweets)):
        answeredtweets[i] = answeredtweets[i].replace("\n", "")
    switch = False
    for i in answeredtweets:
        if tweet[2] == i:
            switch = True
        elif tweet[1] == "der_tony_stark":
            switch = True
        else:
            pass
    return switch


def mark_tweet_done(tweet):  # Expects single tweet (list)
    f = open("answered.txt", "r")
    answeredtweets = f.readlines()
    f.close()
    answeredtweets.append(tweet[2])
    f = open("answered.txt", "w")
    for x in answeredtweets:
        f.write(x + "\n")
    f.close()


def tell_joke(tweet):    # Expects single tweet (list)
    # Quelle http://www.dailymail.co.uk/news/article-1322475/Researchers-official-50-funniest-jokes-time.html
    f = open("twitterjokes.txt", "r")
    jokes = f.readlines()
    f.close()
    while True:
        joke = str("@" + tweet[0] + " " + jokes[randint(0, 37)])
        if len(joke) <= 140:
            reply_semiman(joke, tweet[2])
            break
        else:
            pass


def tell_time(tweet):    # Expects single tweet (list)
    text = str("@" + tweet[0] + " The current time is " + time.ctime()[-13:-5])
    reply_semiman(text, tweet[2])

