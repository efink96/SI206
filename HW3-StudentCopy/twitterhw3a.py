# Write a Python file that uploads an image to your 
# Twitter account.  Make sure to use the 
# hashtags #UMSI-206 #Proj3 in the tweet.

# You will demo this live for grading.

import tweepy

access_token = "307613893-rH7jy1CrmHoBPOTg8aupfO352wakyAiKE8GZWB9n"
access_token_secret = "y5FQ8j9pzdzED1XMyTfYJzdOj9cOg5ZbAhlfnlk4oyaPs"
consumer_key = "D31bG4p7VXi2Hu7kJb2A3FaII"
consumer_secret = "WsrTov0E25jdeGXaswhXF4CgF8Ie004sWq6w9XKnlRyjTMOUTq"

auth = tweepy.OAuthHandler(consumer_key,consumer_secret)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth)
# Question: is it okay that I hard-coded the image?
image = open('elle woods.jpg', 'rb')
img = 'elle woods.jpg'
api.update_with_media(img, status="Love Elle Woods! #UMSI-206 #Proj3 #tweetedusingpython")

print("""Success!""")