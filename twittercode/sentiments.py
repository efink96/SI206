import tweepy
from textblob import TextBlob

# Unique code from Twitter
access_token = "307613893-rH7jy1CrmHoBPOTg8aupfO352wakyAiKE8GZWB9n"
access_token_secret = "y5FQ8j9pzdzED1XMyTfYJzdOj9cOg5ZbAhlfnlk4oyaPs"
consumer_key = "D31bG4p7VXi2Hu7kJb2A3FaII"
consumer_secret = "WsrTov0E25jdeGXaswhXF4CgF8Ie004sWq6w9XKnlRyjTMOUTq"

# Boilerplate code here
auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
#Now we can Create Tweets, Delete Tweets, and Find Twitter Users

public_tweets = api.search('"Gilmore Girls" @netflix')

for tweet in public_tweets:
	print(tweet.text.encode("ascii", "ignore").decode("utf-8"))
	analysis = TextBlob(tweet.text.encode("ascii", "ignore").decode("utf-8"))
	print(analysis.sentiment)


#polarity -- measures how positive or negative
#subjectivity -- measures how factual.

#1 Sentiment Analysis - Understand and Extracting Feelings from Data
