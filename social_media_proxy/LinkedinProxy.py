from linkedin_api.clients.restli.client import RestliClient
from linkedin_api.clients.auth.client import AuthClient

# https://github.com/linkedin-developers/linkedin-api-python-client
# https://learn.microsoft.com/en-us/linkedin/consumer/integrations/self-serve/share-on-linkedin?context=linkedin%2Fconsumer%2Fcontext

class LinkedinProxy():
    def __init__(self, client_id, client_secret):
        self._client = RestliClient()
        self._auth = AuthClient(client_id=client_id, client_secret=client_secret)
        self._access_token = self._auth.get_two_legged_access_token()

    def create_post(self):
        response = self._client.create(
            resource_path="/ugcPosts",
            access_token=self._access_token,
            entity={
                "lifecycleState": "PUBLISHED",
                "specificContent": {
                    "com.linkedin.ugc.ShareContent": {
                        "shareCommentary": {
                            "text": "Hello World! This is my first Share on LinkedIn!"
                        },
                        "shareMediaCategory": "NONE"
                    }
                },
                "visibility": {
                    "com.linkedin.ugc.MemberNetworkVisibility": "PUBLIC"
                }
            }
            
        )
        return response