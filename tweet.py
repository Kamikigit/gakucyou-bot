import random
import tweepy
import api
import datetime
import schedule
import time

auth = tweepy.OAuthHandler(api.CONSUMER_KEY, api.CONSUMER_SECRET)
auth.set_access_token(api.ACCESS_TOKEN, api.ACCESS_SECRET)

api = tweepy.API(auth)

def tweet():
    column = open("column.txt", "r")
    texts = column.read().split("。")
    tweet = random.choice(texts)
    api.update_status(tweet)

schedule.every().hour.do(tweet)

while True:
    schedule.run_pending()
    time.sleep(60)
