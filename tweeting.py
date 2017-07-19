# My Twitter routines
from authenticating import readconf
import tweepy
from random import randint, choice
import time
import pickle
from ddate.base import DDate
from itertools import cycle
import urllib.request


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


def retweet_by_filter(filterword):  # expects list
    tweets = timeline()
    for i in tweets:
        for j in filterword:
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
    commands = ["tell me a joke", "tell me the time", "tell me the discordian date", "play russian roulette",
                "tell my fortune", "My name is Guybrush Threepwood. Prepair to die"]
    if commands[0].lower() in tweet[1].lower():
        tell_joke(tweet)
        mark_tweet_done(tweet)
    elif commands[1].lower() in tweet[1].lower():
        tell_time(tweet)
        mark_tweet_done(tweet)
    elif commands[2].lower() in tweet[1].lower():
        discordian_date(tweet)
        mark_tweet_done(tweet)
    elif commands[3].lower() in tweet[1].lower():
        russian_roulette(tweet)
        mark_tweet_done(tweet)
    elif commands[4].lower() in tweet[1].lower():
        fortunecoockie(tweet)
        mark_tweet_done(tweet)
    elif commands[5].lower() in tweet[1].lower():
        insult(tweet)
        mark_tweet_done(tweet)
    else:
        pass


def check_if_done(tweet):  # Expects single tweet (list)
    with open("answered.list", "rb") as f:
        answeredtweets = pickle.load(f)
    if len(answeredtweets) > 50:
        for i in range(0, 25):
            del answeredtweets[0]
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
    with open("answered.list", "rb") as fr:
        answeredtweets = pickle.load(fr)
    answeredtweets.append(tweet[2])
    with open("answered.list", "wb") as fw:
        pickle.dump(answeredtweets, fw)


def tell_joke(tweet):  # Expects single tweet (list)
    # Quelle http://www.dailymail.co.uk/news/article-1322475/Researchers-official-50-funniest-jokes-time.html
    f = open("twitterjokes.txt", "r")
    jokes = f.readlines()
    f.close()
    while True:
        joke = str("@" + tweet[0] + " " + jokes[randint(0, 36)])
        if len(joke) <= 140:
            # print(joke)
            reply_semiman(joke, tweet[2])
            break
        else:
            pass


def tell_time(tweet):  # Expects single tweet (list)
    text = str("@" + tweet[0] + " The current time is " + time.ctime()[-13:-5])
    # print(text)
    reply_semiman(text, tweet[2])


def discordian_date(tweet):  # Expects single tweet (list)
    text = str("@" + tweet[0] + " " + str(DDate()))
    # print(text)
    reply_semiman(text, tweet[2])


def russian_roulette(tweet):  # Expects single tweet (list)
    alive = True
    chamber = [0, 1, 2, 3, 4, 5]
    loaded = choice(chamber)
    player = [tweet[0], "der_tony_stark"]
    change = cycle((0, 1))
    i = next(change)
    text = ("@" + player[i] + " You starts. ")
    text0, text1 = "", ""
    while alive:
        shot = choice(chamber)
        if shot == loaded:
            text += ("Drehen... BANG! @" + player[i] + " is dead! ")
            alive = False
        else:
            i = next(change)
            text += ("Drehen... Abrücken... @" + player[i] + " ist dran. ")
            chamber.remove(shot)
        if len(text) < 140:
            text0 = text
        else:
            text1 = text[(len(text0)):]
    if len(text) < 140:
        reply_semiman(text, tweet[2])
    elif len(text) >= 140:
        reply_semiman((text0 + "..."), tweet[2])
        reply_semiman(("@" + tweet[0] + "... " + text1), tweet[2])


def fortunecoockie(tweet):  # Expects single tweet (list)
    while True:
        f = urllib.request.urlopen("http://www.dein-glueckskeks.de/glueckskeks-spruch.php")
        fortune = f.read()

        fortune = fortune.decode("ISO-8859-1")
        f.close()

        start = fortune.find("<b>")
        end = fortune.find("</b>")
        text = ("@" + tweet[0] + " " + fortune[(start + 3):end])
        if len(text) < 140:
            break
        else:
            pass
    reply_semiman(text, tweet[2])


def insult(tweet):  # Expects single tweet (list)
    with open("insults.list", "rb") as f:
        insults = pickle.load(f)
    text = ("@" + tweet[0] + " " + choice(insults))
    reply_semiman(text, tweet[2])
    # print(text)