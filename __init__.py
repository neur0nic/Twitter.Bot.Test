import time  # , sys
import tweeting as t


def __main__():
    t.expect_command()
    time.sleep(60)


while True:
    try:
        t.bot_on()
        __main__()
    except KeyboardInterrupt():
        t.bot_off()

