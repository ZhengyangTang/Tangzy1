  
import tweepy  
import requests
import urllib
import sys

#input keys and secret keys  
consumer_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  
consumer_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  
access_key = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  
access_secret = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx'  
  
# upload keys and secret keys
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
auth.set_access_token(access_key, access_secret)  
  
api = tweepy.API(auth)  
  
#get user's first 10 images from first 200 tweets 
def get_tweets(screen_name):
	count = 0;
	public_tweets = api.user_timeline(screen_name = screen_name,count = 200)  
	for tweet in public_tweets:
		if 'media' in tweet.entities.keys(): 	  
			urllib.request.urlretrieve(tweet.entities['media'][0]['media_url'],'C:/0%d.jpg'%count)
			count = count + 1
			if count == 10:
				break
if __name__ == '__main__':
	get_tweets(sys.argv[1])
  
