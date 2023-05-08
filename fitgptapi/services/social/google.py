import requests
from munch import DefaultMunch as munch
from ...models import UserAccountInfo

class Google():
    GOOGLE_OAUTH_URL = 'https://www.googleapis.com/oauth2/v3'
    def __init__(self, user_profile):
        self.user_profile = user_profile

    # {
    #   'sub': '110457415105910494871',
    #   'name': 'Adrian Cowham',
    #   'given_name': 'Adrian',
    #   'family_name': 'Cowham',
    #   'picture': 'https://lh3.googleusercontent.com/a/AGNmyxbYk9V6o5RlQRUKdUJrlVNJTTRR9jfhDYCUJ7fL=s96-c',
    #   'email': 'adrian.cowham@gmail.com',
    #   'email_verified': True,
    #   'locale': en'
    # }
    def get_user(self):
        params = {'access_token': self.user_profile.access_token}
        response = requests.get(self.GOOGLE_OAUTH_URL + '/userinfo', params=params)
        if response.status_code == 200:
            user = munch.fromDict(response.json())
            if user.sub == self.user_profile.sub:
                return UserAccountInfo(user.given_name, user.family_name, user.email)
            else:
                return None
        else:
            return None