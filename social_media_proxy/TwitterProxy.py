# from .Proxy import Proxy
import tweepy
import os
from dotenv import load_dotenv
load_dotenv()


class TwitterProxy():
    def __init__(self, access_token, access_token_secret):
        self._client = tweepy.Client(
            bearer_token=os.getenv("BEARER_TOKEN"),
            consumer_key=os.getenv("API_KEY"),
            consumer_secret=os.getenv("API_KEY_SECRET"),
            access_token=access_token,
            access_token_secret=access_token_secret,
        )
    
    def get_me(self):
        return self._client.get_me().data.data
    
    def create_tweet(self, text):
        return self._client.create_tweet(
            text=text,

        ).data
    
    def detete_tweet(self, id):
        return self._client.delete_tweet(
            id=id,
        ).data
