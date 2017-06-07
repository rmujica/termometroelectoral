import tweepy
import csv

consumer_key = "ukAOIzYxwxPtp3VgbN078rfRu"
consumer_secret = "UlaHr1HiyuAG0IW0QJigy0XV7KXptU499J3CfiTqkRlMYFZOTl"
access_token = "14500149-JsySAhg9m6lK1HnWGLBvEnhlEHy1lflbO91IT3cPE"
access_token_secret = "RUiTTa3A8CvOWbKDrvAXPddtMbO3qPUeO1njBZtdUOuWo"

def get_tweets(username, starting=None, append=False):
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    api = tweepy.API(auth)

    tweets = []
    if starting:
        new_tweets = api.user_timeline(screen_name=username, count=200, max_id=starting)
    else:
        new_tweets = api.user_timeline(screen_name=username, count=200)

    tweets.extend(new_tweets)
    oldest = tweets[-1].id - 1

    while len(new_tweets) > 0:
        new_tweets = api.user_timeline(screen_name=username, count=200, max_id=oldest)
        tweets.extend(new_tweets)
        oldest = tweets[-1].id - 1
        print(str(len(tweets)), "tweets downloaded so far, current oldest: " + str(oldest))

    transformed = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in tweets]

    if append:
        with open(username + "_tweets.csv", "a") as f:
            writer = csv.writer(f)
            writer.writerows(transformed)
    else:
        with open(username + "_tweets.csv", "w") as f:
            writer = csv.writer(f)
            writer.writerow(["id", "created_at", "text"])
            writer.writerows(transformed)

#get_tweets("labeasanchez", starting=676941073906839552, append=True)
get_tweets("Fr_parisi")