import tweepy
import nltk

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

public_tweets = api.search('UMSI')


adj_count = 0;

for tweet in public_tweets:
	print(tweet.text.encode("ascii", "ignore").decode("utf-8"))
	tagged_tokens = nltk.pos_tag(tweet.text.encode("ascii", "ignore").decode("utf-8")) # gives us a tagged list of tuples
	for (word, tag) in tagged_tokens:
		if tag == "JJ":
			adj_count+=1

print("There were ", adj_count,"adjectives in your tweets")
	
#Learn more about Search
#https://dev.twitter.com/rest/public/search

