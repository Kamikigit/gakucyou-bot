import random
import tweepy
import datetime
import schedule
import time

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_TOKEN,_KEY, ACCESS_TOKEN_SECRET)

api = tweepy.API(auth)

def tweet():
    with open("column.txt", "r") as f:
        texts = f.read().split("。")    
    tweet = random.choice(texts)
    print(tweet)
    api.update_status(tweet)

schedule.every().hour.do(tweet)

while True:
    schedule.run_pending()
    time.sleep(60)

