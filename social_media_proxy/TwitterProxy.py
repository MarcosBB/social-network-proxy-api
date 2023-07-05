# from .Proxy import Proxy
import tweepy

class TwitterProxy():
    def __init__(self, bearer_token):
        self.client = tweepy.Client(
            bearer_token=bearer_token
        )
    
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
    
    @classmethod
    def token(consumer_key, consumer_secret):
        auth = tweepy.OAuth2AppHandler(
            consumer_key, 
            consumer_secret,
        )
        return {"bearer_token": auth.apply_auth().bearer_token}