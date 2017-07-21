import tweepy
from textblob import TextBlob

consumer_key = '7VeUl1g66CjKptK3qrb6Fgqgl'
consumer_secret = 'ZFxlmuFOgquZeU10GCRXXZMdexV2Du5oSj7koxUTKKLqQ7OLR6'

access_token = '84179899-zCzJZxuw4i6e68vy9WPW45UXuvYgHPTMEZX0WmSxD'
access_token_secret = 'ucSRkOdSFv04OqvninV7V676Fvo62DiC3Tgd3g9VZuqd3'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

# Tweepy API function
api = tweepy.API(auth)

# sentiment analysis function, that takes in a string, calls the api.search method and runs a seniment analysis on the tweet,
# it prints out how many positive,negative, and neutral tweets there were about that search call in the last 30 tweets
def sentimentSearchAnalysis(key):
    public_tweet = api.search(key, count=100)
    pos_count = 0
    neg_count = 0
    neut_count = 0
    for tweet in public_tweet:
        analysis = TextBlob(tweet.text)
        if analysis.sentiment.polarity > 0:
            pos_count += 1
        if analysis.sentiment.polarity < 0:
            neg_count += 1
        if analysis.sentiment.polarity == 0:
            neut_count += 1
    ret_dict = {'keyword': key, 'positive': pos_count, 'negative': neg_count, 'neutral': neut_count}
    return ret_dict

print(sentimentSearchAnalysis(keyWord))