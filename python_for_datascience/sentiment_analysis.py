import tweepy
from textblob import TextBlob

# Challenge
# Instead of printing out each tweet, save each Tweet to a CSV file with an associated label.
# The label should be either 'Positive' or 'Negative'.
# You can define the sentiment polarity threshold yourself,
# whatever you think constitutes a tweet being positive/negative.

# get info from https://developer.twitter.com/en/apps/15955270
consumer_key = ''
consumer_secrete = ''

access_token = ''
access_token_secrete = ''

auth = tweepy.OAuthHandler(consumer_key, consumer_secrete)
auth.set_access_token(access_token, access_token_secrete)

api = tweepy.API(auth)


# label the sentiments
def get_label(analysis, threshold=0):
  if analysis.sentiment[0] > threshold:
    return 'Positive'
  else:
    return 'Negative'


# retrieve tweets and save them to csv
public_tweets = api.search('Trump')

with open('trump_tweets.csv', 'wb') as sentiments_file:
  sentiments_file.write('tweet,sentiment_label\n'.encode('utf8'))
  for tweet in public_tweets:
    analysis = TextBlob(tweet.text)
    csv_row = '%s,%s\n' % (tweet.text.encode('utf8'), get_label(analysis))
    sentiments_file.write(csv_row.encode('utf-8'))
