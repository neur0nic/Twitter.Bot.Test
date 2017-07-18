from create_login_cfg import create


def readconf():
    while True:
        try:
            # int("hallo")
            f = open("login_sec.cfg", "r")  # muss "login.cfg" heissen
            consumer_key = f.readline().split(" ")[-1].replace("\n", "")
            consumer_secret = f.readline().split(" ")[-1].replace("\n", "")
            access_token = f.readline().split(" ")[-1].replace("\n", "")
            access_token_secret = f.readline().split(" ")[-1].replace("\n", "")
            keys = [consumer_key, consumer_secret, access_token, access_token_secret]
            f.close()
            # print("Success!\n")
            break
        except:
            print("Login not configured yet.")
            create()
    return keys
