import tweepy
import datetime
import json
import sqlite3

import os
from dotenv import load_dotenv
from pathlib import Path

env_path = Path('.') / '.env'
load_dotenv(dotenv_path=env_path)

class Tweet:
    def __init__(self, tweet_data):
        tweet = tweet_data._json
        self.id = tweet['id']
        self.full_text = tweet['full_text']
        self.retweet_count = tweet['retweet_count']
        self.favorite_count = tweet['favorite_count']
        self.user = {
            'id': tweet['user']['id'],
            'name': tweet['user']['name'],
            'screen_name': tweet['user']['screen_name'],
            'followers_count': tweet['user']['followers_count'],
            'friends_count': tweet['user']['friends_count'],
            'listed_count': tweet['user']['listed_count'],
            'favourites_count': tweet['user']['favourites_count'],
            'statuses_count': tweet['user']['statuses_count'],
            'profile_image_url': tweet['user']['profile_image_url'],
        }
    
    def get_tweet_data(self):
        return (
            self.id, 
            self.full_text, 
            self.retweet_count,
            self.favorite_count,
            self.user['id']
        )
        
    def get_tweet_user_data(self):
        return (
            self.user['id'],
            self.user['name'],
            self.user['screen_name'],
            self.user['followers_count'],
            self.user['friends_count'],
            self.user['listed_count'],
            self.user['favourites_count'],
            self.user['statuses_count'],
            self.user['profile_image_url'],
        )

    def get_tweet_user_id(self):
            return self.user['id']


def get_tweet_data(keyword, use_retweet):
    #python で Twitter APIを使用するためのConsumerキー、アクセストークン設定
    Consumer_key = os.getenv('TWITTER_CONSUMER_KEY')
    Consumer_secret = os.getenv('TWITTER_CONSUMER_SECRET')
    Access_token = os.getenv('TWITTER_ACCESS_TOKEN')
    Access_secret = os.getenv('TWITTER_ACCESS_SECRET')

    auth = tweepy.OAuthHandler(Consumer_key, Consumer_secret)
    auth.set_access_token(Access_token, Access_secret)

    api = tweepy.API(auth, wait_on_rate_limit = True)

    q = keyword
    if use_retweet == False:
        q += ' -RT'

    tweet_list =[]

    for tweet in tweepy.Cursor(api.search, q=q, count=100, tweet_mode='extended').items(100):
        jsttime = tweet.created_at + datetime.timedelta(hours=9)
        tweet_data = Tweet(tweet)
        tweet_list.append(tweet_data)
    
    db_path = os.getenv('DB_PATH')
    connect = sqlite3.connect(db_path)
    db = connect.cursor()

    insert_tweet_data = []
    for tweet in tweet_list:
        insert_tweet_data.append(tweet.get_tweet_data())

    tmp_user_dict = {}
    for tweet in tweet_list:
        tmp_user_dict[tweet.get_tweet_user_id] = tweet.get_tweet_user_data()
    insert_user_data = []
    for key in tmp_user_dict:
        insert_user_data.append(tmp_user_dict[key])

    try:
        db.execute("DELETE FROM tweet_data")
        db.execute("DELETE FROM tweet_user")
        db.executemany("INSERT INTO tweet_data VALUES (?,?,?,?,?)", insert_tweet_data)
        db.executemany("INSERT INTO tweet_user VALUES (?,?,?,?,?,?,?,?,?)", insert_user_data)

    except sqlite3.Error as e:
        print(e)

    connect.commit()
    connect.close()

if __name__ == '__main__':

    #検索キーワードを入力  ※リツイートを除外する場合 「キーワード -RT 」と入力
    print ('====== Enter Serch KeyWord   =====')
    keyword = input('>  ')
    get_tweet_data(keyword)
