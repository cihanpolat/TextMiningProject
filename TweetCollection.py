import tweepy
from tweepy import OAuthHandler
import json

from tweepy import Stream
from TweetListner import TweetListner

# In order to authorise our app to access Twitter on our behalf, we need to use the OAuth interface
consumer_key = '9svuPyklf5DdN9UH8gF8tlImW'
consumer_secret = 'lD9y6lMnYGaUukowA3qtUGzr0LcL1xi7uAsrY2rFmjWkYyZHdN'
access_token = '794336771869933568-lIXAwTsfZNEjvEQgJmDzvxIxtuhZTry'
access_secret = '8UShadJx1nZEnCQ5YnVPG4x5Nh9SSRsLf0dLZL133ISh7'

auth = OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

#The api variable is now our entry point for most of the operations we can perform with Twitter.
api = tweepy.API(auth)

twitter_stream = Stream(auth, TweetListner())
twitter_stream.filter(track=['#BTW2017'])

