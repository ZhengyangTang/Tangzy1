  
import tweepy  
import requests
import urllib

#input keys and secret keys  
consumer_key = 'eIdSVPYAdVOSy3aCluX9P9P97'  
consumer_secret = 'EZpKmpK6RpyOSoLEHAubZBh3hud0bZucjIS8WFGR1ISEjT7vhy'  
access_key = '1038545947972780032-viHFmLkInLs79xOxatMU19qcG4SfTh'  
access_secret = '2L6m6hxXwkTgFOYg15SJ1nBe9yxMoPMUY1lHgnIt4JpBO'  
  
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
			#image = requests.get(tweet.entities['media'][0]['media_url'])
			#with open("0%d.jpg"%count,'w') as f:
			#	f.write(image.content)
			urllib.request.urlretrieve(tweet.entities['media'][0]['media_url'],'C:/EC601/EC601_IMAGES/%d.png'%count)
			count = count + 1
			if count == 10:
				break
if __name__ == '__main__':
	get_tweets('@RickandMorty')
  