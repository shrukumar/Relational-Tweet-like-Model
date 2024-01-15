import pandas as pd
import random
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

    def post_tweet(self, tweet):
        sql = "INSERT INTO Tweets (user_id, text) VALUES (%s, %s) "
        val = (tweet.user_id, tweet.tweet_text)
        self.dbu.insert_one(sql, val)

    def get_random_user(self):
        sql = "SELECT DISTINCT user_id AS user FROM Tweets"
        df_users = self.dbu.execute(sql)
        return random.choice(list(df_users))
    
    def get_timeline(self, rand_user):
        sql = f"""
            SELECT Tweets.user_id, tweet_ts, tweet_text FROM Tweets JOIN Follows
            WHERE Follows.user_id = {rand_user}
            ORDER BY tweet_ts DESC
            LIMIT 10
            """
        timeline = self.dbu.execute(sql)
        return timeline


