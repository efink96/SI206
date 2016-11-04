# In this assignment you must do a Twitter search on any term
# of your choice.
# Deliverables:
# 1) Print each tweet
# 2) Print the average subjectivity of the results
# 3) Print the average polarity of the results

# Be prepared to change the search term during demo.
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
search_term = input('Enter a search term: ')
public_tweets = api.search(search_term)

tweet_count = 0
pol_sum = 0
sub_sum = 0
for tweet in public_tweets:
	print(tweet.text.encode("ascii", "ignore").decode("utf-8"))
	analysis = TextBlob(tweet.text.encode("ascii", "ignore").decode("utf-8"))
	tweet_count += 1
	pol_sum += analysis.sentiment.polarity
	sub_sum += analysis.sentiment.subjectivity

avg_pol = pol_sum / tweet_count
avg_sub = sub_sum / tweet_count

print("Average subjectivity is", avg_pol)
print("Average polarity is", avg_sub)
