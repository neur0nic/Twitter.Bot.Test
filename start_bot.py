#!/usr/bin/env python3
# coding: utf-8

import time  # , sys
import tweeting as t
from threading import Thread


def main():
    t.bot_on()
    print("Bot has started. Ready to tweet! ")
    list = []
    abort = Thread(target=stopp, args=(list,))
    abort.start()
    print("Hit 'Return' to stop the bot. ")
    while not list:
        try:
            t.expect_command()
            time.sleep(60)
            # print("jupp")
        except:
            pass
    t.bot_off()
    print("Bot has been stopped. Good bye! ")


def stopp(list):
    input()
    list.append(None)


if __name__ == '__main__':
    main()
