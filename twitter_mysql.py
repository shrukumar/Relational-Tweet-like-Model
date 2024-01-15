import pandas as pd
from dbutils import DBUtils
from tweet_object import Tweet


class TwitterAPI:

    def __init__(self, user, password, database, host="localhost"):
        self.dbu = DBUtils(user, password, database, host)

    def populate_followers(self, file):
        df_followers = pd.read_csv(file)
        for idx, row in df_followers.iterrows():
            sql = "INSERT INTO Follows (user_id, follows_id) VALUES (%s, %s) "
            self.dbu.insert_one(sql, tuple(row))

    def add_tweet(self, tweet):
        sql = "INSERT INTO Tweet (user_id, text) VALUES (%s, %s) "
        val = (tweet.user_id, tweet.tweet_text)
        self.dbu.insert_one(sql, val)

