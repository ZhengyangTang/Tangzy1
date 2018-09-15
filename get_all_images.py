#导入tweepy  
import tweepy  
import json
#填写twitter提供的开发Key和secret  
consumer_key = 'eIdSVPYAdVOSy3aCluX9P9P97'  
consumer_secret = 'EZpKmpK6RpyOSoLEHAubZBh3hud0bZucjIS8WFGR1ISEjT7vhy'  
access_key = '1038545947972780032-viHFmLkInLs79xOxatMU19qcG4SfTh'  
access_secret = '2L6m6hxXwkTgFOYg15SJ1nBe9yxMoPMUY1lHgnIt4JpBO'  
  
#提交你的Key和secret  
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)  
auth.set_access_token(access_key, access_secret)  
  
api = tweepy.API(auth)  
  
#打印其他用户主页上的时间轴里的内容 
def get_tweets(screen_name):
	public_tweets = api.user_timeline(screen_name)  
	for tweet in public_tweets:
		if 'media' in tweet.entities.keys():	  
			print(tweet.entities['media'][0]['media_url'])
if __name__ == '__main__':
	get_tweets('Jimmyfallon')
  