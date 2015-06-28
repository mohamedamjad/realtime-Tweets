# Mohamed Amjad LASRI

# Import the necessary methods from tweepy library
from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream
import sys
from pymongo import MongoClient
import json
from json import dumps

#Variables that contains the user credentials to access Twitter API 
consumer_key = ""
consumer_secret = ""
access_token = ""
access_token_secret = ""


#This is a basic listener that just prints received tweets to stdout.
class StdOutListener(StreamListener):

    def on_data(self, data):
        dict_data = json.loads(data)
        json_data = json.dumps(dict_data, ensure_ascii=False)
        print(collection.save(dict_data))
        return True

    def on_error(self, status):
        print (status)


if __name__ == '__main__':

    # Create a mongo client:
    mongoClient = MongoClient('localhost',27017)

    # Getting the Database
    db = mongoClient['tweets']

    # Getting the Collection
    collection = db['SNCF_COLLECTION']

    #This handles Twitter authetification and the connection to Twitter Streaming API
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    stream = Stream(auth, l)


    #This line filter Twitter Streams to capture data by the keywords: 'python', 'javascript', 'ruby'
    stream.filter(track=sys.argv)
