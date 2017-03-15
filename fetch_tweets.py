from twython import Twython, TwythonError
import time


api_key="XEJB5Rf0AaoLNo4oAsK7oWaG5"
api_secret="dm9BR5nvV74e74wqgzVezDVEm8iDbfZyXtUQ2UdEcH4Gq3dNt7"
access_key="780742606418358272-dbpVU5L9uzyhXk4TTiD5z2nylTq7yiz"
access_secret ="ktQWfh066fJZY1qX0cjansLM5NKjvlzz9f8a1aMVjMbLz"

twitter = Twython(api_key,api_secret, access_key,access_secret)


def user_id(username = ''):
	username = input("\nEnter user's Twitter handle: ")
	return username	

def fetch_tweets(username):
	user_tweets= twitter.get_user_timeline(screen_name = username, count = 50) 
	tweet_text = []


	for tweets in user_tweets:

		tweet_text.append(tweets['text'])
			
		# return(tweet_text)
		return(tweet_text)
		

print(fetch_tweets('realDonaldTrump'))

