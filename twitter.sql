DROP DATABASE IF EXISTS Twitter;
CREATE DATABASE Twitter;

use Twitter; 

CREATE TABLE IF NOT EXISTS Tweet
(
    tweet_id INT PRIMARY KEY AUTO_INCREMENT,
    user_id INT,
    tweet_ts TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    tweet_text VARCHAR(140)
    )

CREATE TABLE IF NOT EXISTS Follows
(
    user_id INT,
    follows_id INT
)

