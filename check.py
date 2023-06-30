import tweepy
from config import *
import json

auth = tweepy.OAuthHandler(consumer_key=API_KEY, consumer_secret=API_KEY_SECRET, access_token=ACCESS_TOKEN,
                           access_token_secret=ACCESS_TOKEN_SECRET)
api = tweepy.API(auth)
user = api.verify_credentials(include_entities=True, skip_status=False, include_email=True)
print(json.dumps(user._json, indent=4))
