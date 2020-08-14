import random
import tweepy
import datetime
import schedule
import time
import os

auth = tweepy.OAuthHandler(os.environ["CONSUMER_KEY"], os.environ["CONSUMER_SECRET"])
auth.set_access_token(os.environ["ACCESS_TOKEN_KEY"], os.environ["ACCESS_TOKEN_SECRET"])

api = tweepy.API(auth)

def tweet():
    with open("column.txt", "r") as f:
        texts = f.read().split("。")    
    tweet = random.choice(texts)
    print(tweet)
    api.update_status(tweet)


def follow():
    follower_list = api.followers()
    for follower in follower_list:
        des = follower.description
        if "ネットビジネス" | "副業" in des:
            pass
        else:
            follower_id = follower.id
            api.create_friendship(follower.id)

if __name__ == "__main__":
    # schedule.every().day.at("9:00").do(tweet)
    tweet()
    follow()
    

# while True:
#     schedule.run_pending()
#     time.sleep(60)

