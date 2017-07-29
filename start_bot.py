#!/usr/bin/env python3
# coding: utf-8

import time  # , sys
from os import system
import tweeting
from threading import Thread
from create_login_cfg import first_start


def main():
    t = tweeting.TweetClass()
    t.bot_on()
    print("Bot has started. Ready to tweet! ")
    list = []
    abort = Thread(target=stopp, args=(list,))
    abort.start()
    print("Hit 'Return' to stop the bot. ")
    while not list:
        try:
            t.expect_command()
            t.retweet_follower()
            time.sleep(60)
            # print("jupp")
        except:
            pass
    t.bot_off()
    print("Bot has been stopped. Good bye! ")
    system("exit")


def stopp(list):
    input()
    list.append(None)


if __name__ == '__main__':
    first_start()
    main()

