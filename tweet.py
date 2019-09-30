from auth import keys
import tweepy

auth = keys()
api = tweepy.API(auth, wait_on_rate_limit=True,
                 wait_on_rate_limit_notify=True)

api.update_status("This is a test tweet from the Tweepine Bot")
