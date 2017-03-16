from watson_developer_cloud import AlchemyLanguageV1
from alchemy_sentiment import api_key as ak

alchemy_language = AlchemyLanguageV1(api_key=ak)



class Sentiment:


	def getSentiment(tweet):
	    try:
	        result = alchemy_language.sentiment(text=tweet)
	        if result['status'] == 'OK':
	            sentimentsList = []
	            for item in result['docSentiment'].items():
	                sentimentsList.append(item[0] + ": " + item[1])
	            return sentimentsList

	    except Exception:
	        return []