"""
J. Rachlin
Demonstration of working with Relational Database with python
"""

import os
import pandas as pd
from twitter_mysql import TwitterAPI
from tweet_object import Tweet

def main():

    # Authenticate
    api = TwitterAPI(os.environ["TWITTER_USER"], os.environ["TWITTER_PASSWORD"], "twitter")

    # add follower data 
    api.populate_followers("follows_sample.csv")

    # add tweets
    df_tweets = pd.read_csv("tweets_sample.csv")
    for idx, row in df_tweets.iterrows():
        api.post_tweet(Tweet(user_id = row[0], tweet_text = row[1]))
        

    


if __name__ == '__main__':
    main()