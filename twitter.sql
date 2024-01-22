DROP SCHEMA Twitter;

CREATE SCHEMA Twitter;

USE Twitter;

DROP TABLE IF EXISTS Tweets;

CREATE TABLE IF NOT EXISTS Tweets
(
    tweet_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    tweet_ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    tweet_text VARCHAR(140)
    );

DROP TABLE IF EXISTS Follow;

CREATE TABLE IF NOT EXISTS Follow
(
    user_id INT,
    follows_id INT
);
