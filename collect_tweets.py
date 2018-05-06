import tweepy
import csv
import sys
#These are obtained from the app created at Twitter dev zone. You need them for this program to work
#Please create an app and fill in these credentials before running this program
ckey = "AwcLLtYIeWoEN77tC7sHcP2Yo"
csecret = "iPSakaY0cAdXhnDM9cmV8DPuShfuE1L7LYTjnAZJmgvSMRSINC"
akey = "3278300185-mRhhSr3A86jnmKUAnkacskqLrQPYqloLzzzvsEa"
asecret = "kz44vubMmzUMT0Mk8sM5HlLJCpWNVqNnu94VneyO9mX6a"

def get_all_tweets(screen_name):
	#authorize twitter, initialize tweepy
	auth = tweepy.OAuthHandler(ckey, csecret)
	auth.set_access_token(akey, asecret)
	api = tweepy.API(auth)
	#initialize a list to hold all the tweepy Tweets
	tweets = []
	#make initial request for most recent tweets (200 is the maximum allowed count)
	new_tweets = api.user_timeline(screen_name = screen_name,count=200)
	#save most recent tweets
	tweets.extend(new_tweets)
	#save the id of the oldest tweet less one
	oldest = tweets[-1].id - 1
	#keep grabbing tweets until there are no tweets left to grab
	while len(new_tweets) > 0:
		print "getting tweets before %s" % (oldest)
		#all subsiquent requests use the max_id param to prevent duplicates
		new_tweets = api.user_timeline(screen_name = screen_name,count=200,max_id=oldest)
		#save most recent tweets
		tweets.extend(new_tweets)
		#update the id of the oldest tweet less one
		oldest = tweets[-1].id - 1
		print "...%s tweets downloaded so far" % (len(tweets))
	#transform the tweepy tweets into a 2D array that will populate the csv
	outtweets = [[tweet.id_str, tweet.created_at, tweet.text.encode("utf-8")] for tweet in tweets]
	#write the csv
	with open('%s_tweets.csv' % screen_name, 'wb') as f:
		writer = csv.writer(f)
		writer.writerow(["id","created_at","text"])
		writer.writerows(outtweets)
	pass
if __name__ == '__main__':
	#pass in the username of the account you want to download
	get_all_tweets(sys.argv[1])
