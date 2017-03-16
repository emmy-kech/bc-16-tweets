import time
import json
# import pdb

from watson_developer_cloud import AlchemyLanguageV1
from  sentiment01 import Sentiment
from tqdm import tqdm
from collections import Counter
from twython import Twython, exceptions


class TwitterUser:

    def __init__(self):
        api_key = "XEJB5Rf0AaoLNo4oAsK7oWaG5"
        api_secret = "dm9BR5nvV74e74wqgzVezDVEm8iDbfZyXtUQ2UdEcH4Gq3dNt7"
        access_key = "780742606418358272-dbpVU5L9uzyhXk4TTiD5z2nylTq7yiz"
        access_secret = "ktQWfh066fJZY1qX0cjansLM5NKjvlzz9f8a1aMVjMbLz"

        self.twitter = Twython(api_key, api_secret, access_key, access_secret)

    def user_id(self):
        username = input("\nEnter user's Twitter handle: ")
        return username

    def fetch_tweets(self, username=''):
        try:
            username = self.user_id()
            user_tweets = self.twitter.get_user_timeline(
                screen_name=username, count=15)
            tweet_text = []
            output= ' '
            bar = tqdm(total=int(len(user_tweets)))
            for tweets in user_tweets:
                time.sleep(0.1)
                tweet_text.append(tweets['text'])
                output += (tweets['text']+'\n')
                bar.update(1)
                sentiment= Sentiment.getSentiment(tweets)
                print (sentiment)

            bar.close()
            with open('tweets.json', 'w') as f:
                json.dump(tweet_text, f, indent=4)
            return output
        except Exception as e:
            print("User does not exist")
            self.fetch_tweets() #recursion

    def word_count(self, tweet_list):

        output = ''
        for results in tweet_list:
            output += results
        word_list = output.split(' ')
        c = Counter(word_list)
        return c.most_common(5)

def main():
    tweet = TwitterUser()
    tweets = tweet.fetch_tweets()
    word_count = tweet.word_count(tweets)
    print(tweets)
    print(word_count)


if __name__ == '__main__':
    main()
