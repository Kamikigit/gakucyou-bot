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

schedule.every().day.at("9:00").do(tweet)
schedule.every().day.at("10:00").do(tweet)
schedule.every().day.at("13:00").do(tweet)
schedule.every().day.at("15:00").do(tweet)
schedule.every().day.at("17:00").do(tweet)


while True:
    schedule.run_pending()
    time.sleep(60)

