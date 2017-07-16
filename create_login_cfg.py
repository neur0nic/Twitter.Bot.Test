# Creating new Twitter login cfg
import os
import help_functions


def create():
    if test_new() is 1:
        test_exist()
        input_parameters()
    else:
        print("No loginfile has been created.\n")


def test_new():  # Ask if new Config should be created
    while True:
        try:
            answer = input("Create a new loginfile? (Y/N) ")
            if answer is "Y":
                del answer
                x = 1
                break
            elif answer is "N":
                del answer
                x = 0
                break
            else:
                del answer
                pass
        except:
            pass
    return x


def test_exist():  # Test if config already exist
    directory = os.listdir()
    if "login.cfg" in directory:
        print("Loginfile already exists.")
        while True:
            try:
                answer = input("Moving login.cfg to login.cfg-old? Loginfile deleted when No. (Y/N) ")
                if answer is "Y":
                    os.renames("login.cfg", "login.cfg-old")
                    del answer
                    break
                elif answer is "N":
                    os.remove("login.cfg")
                    del answer
                    break
                else:
                    del answer
                    pass
            except:
                pass
    else:
        pass


def input_parameters():  # Entering Tokens and Secrets
    while True:
        try:
            consumer_key = input("Input your Consumer Key: ")
            consumer_secret = input("Input your Consumer Secret: ")
            access_token = input("Input your Access Token: ")
            access_secret = input("Input your Access Secret: ")
            break
        except:
            print("Invalid input! Try again.")
            pass
    fw = open("login.cfg", "w")
    fw.write("consumer_key = " + consumer_key + "\n")
    fw.write("consumer_secret = " + consumer_secret + "\n")
    fw.write("access_toke = " + access_token + "\n")
    fw.write("access_token_secret = " + access_secret + "\n")
    fw.close()
    print("Configuration complete!\n")
