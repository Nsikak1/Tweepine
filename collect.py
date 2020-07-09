import tweepy as tw
from auth import keys

api = tw.API(keys(), wait_on_rate_limit=True)

twitter_handle = "xyluz"

#  initial request for most recent tweets (200 is the maximum allowed count)
user = api.get_user(twitter_handle)
print(user.name)
print(user.description)
print(user.location)
