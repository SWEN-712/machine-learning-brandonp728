# Databricks notebook source
from tweepy import OAuthHandler
from tweepy import API
from tweepy import Cursor
import json

consumer_key = "I1P8tfIDH5zgsoZySN7GzgAFA"
consumer_secret = "zpk5h3HBcPgVGu5OTRI6dJt1irDsRpJdrmUZEqfYLkbjLekqub"
access_token = "313711762-du6xzU82dgzzJaxEsiz3DSUJlVZNXKYrqpivvj3E"
access_token_secret = "5gDZy6HmeMCgSkzONOVEiywoRFTT7fNNRRaDu0Yv7WToX"

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
auth_api = API(auth)

google_access_tweets = auth_api.user_timeline(screen_name="googleaccess", count=600, include_rts=False, tweet_mode="extended")
final_tweets = [tweet.full_text for tweet in google_access_tweets]

with open('/dbfs/google_access_tweets.txt', 'w') as f:
  for item in final_tweets:
      f.write("%s\n" % item)
