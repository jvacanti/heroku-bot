# Dependencies
import tweepy
import json
import time

# Twitter API Keys
consumer_key = "0tIBNyPJJ2IxMNKMouQxJTAFy"
consumer_secret = "IOtTY5vnmTmBB688toZbE8FNx5Zt2vHYqDl5vvFpzBhPB5dXY0"
access_token = "109056014-JAdDs3jliSmaF7JgmBGtamTPnPBMtOVbMLsejyXb"
access_token_secret = "Em7DqDMsUbjs23sZKdepwBf66reriJGGPvcSttFNIj0IT"

# Setup Tweepy API Authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth, parser=tweepy.parsers.JSONParser())


# Create a function that tweets
# CODE GOES HERE