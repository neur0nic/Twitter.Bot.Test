# Creating new Twitter login cfg
import os
import pickle


def create():
    if test_new():
        test_exist()
        input_parameters()
    else:
        print("No loginfile has been created.\n")


def test_new():  # Ask if new Config should be created
    while True:
        try:
            answer = input("Create a new loginfile? (Y/N) ")
            if answer.upper() == "Y":
                del answer
                x = True
                break
            elif answer.upper() == "N":
                del answer
                x = False
                break
            else:
                del answer
                pass
        except:
            pass
    return x


def test_exist():  # Test if config already exist
    wdir = os.path.expanduser("~") + "/.moehp/"
    config = os.path.expanduser("~") + "/.moehp/login.cfg"
    if "login.cfg" in wdir:
        print("Loginfile already exists.")
        while True:
            try:
                answer = input("Moving login.cfg to login.cfg-old? Loginfile deleted when No. (Y/N) ")
                if answer.upper() is "Y":
                    os.renames(config, (config + "-old"))
                    del answer
                    break
                elif answer.upper() is "N":
                    os.remove(config)
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
    config = os.path.expanduser("~") + "/.moehp/login.cfg"
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
    fw = open(config, "w")
    fw.write("consumer_key = " + consumer_key + "\n")
    fw.write("consumer_secret = " + consumer_secret + "\n")
    fw.write("access_toke = " + access_token + "\n")
    fw.write("access_token_secret = " + access_secret + "\n")
    fw.close()
    print("Configuration complete!\n")


def first_start():
    wdir = os.path.expanduser("~") + "/.moehp/"
    config = os.path.expanduser("~") + "/.moehp/login.cfg"
    try:
        os.listdir(wdir)
    except:
        os.mkdir(wdir)
        emptylist = ['testdata']
        with open((wdir + "answered.list"), "wb") as f:
            pickle.dump(emptylist, f)
        # os.system("touch " + config)
