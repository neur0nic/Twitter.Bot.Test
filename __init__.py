import time  # , sys
import tweeting as t


def __main__():
    while True:
        t.tweet_semiman(time.ctime() + ": This is a testrun.")
        time.sleep(60)


try:
    __main__()
except:
    print("__main__() is not starting.\n")
