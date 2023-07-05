# from .Proxy import Proxy
import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

class TwitterProxy():
    def __init__(self):
        self.client = tweepy.Client(
            bearer_token=os.getenv("BEARER_TOKEN"),
            consumer_key=os.getenv("API_KEY"),
            consumer_secret=os.getenv("API_KEY_SECRET"),
            access_token=os.getenv("ACCESS_TOKEN"),
            access_token_secret=os.getenv("ACCESS_TOKEN_SECRET"),
        )
        
        # self.auth = tweepy.OAuth2AppHandler(
        #     os.getenv("API_KEY"), 
        #     os.getenv("API_KEY_SECRET"),
        # )
        
        # self.auth.set_access_token(
        #     os.getenv("ACCESS_TOKEN"),
        #     os.getenv("ACCESS_TOKEN_SECRET"),
        # )

        # self.api = tweepy.API(self.auth)
    
    def get_me(self):
        return self.client.get_me().data.data
    
    def create_tweet(self, text):
        return self.client.create_tweet(
            text=text,

        ).data
    
    def detete_tweet(self, id):
        return self.client.delete_tweet(
            id=id,
        ).data


twitter = TwitterProxy()
import pdb; pdb.set_trace()