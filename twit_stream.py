
from __future__ import absolute_import, print_function

from tweepy.streaming import StreamListener
from tweepy import OAuthHandler
from tweepy import Stream

consumer_key = 'Nr8T2KjCOXekr14xx4ItNH45i' 
consumer_secret = '8LOj06y3XzH71XfWvTEcQXiv62esaz7gf1nIZ8511A5rFKLwTz'  
access_token =  '2811921162-1KseWeQz1SzDifVMa8AK6qsRhtTXmhhxl51n4JY'  
access_token_secret = 'umXUAWDXxUtcfjonNft1tcp3m8VVknXUW3ajVSbLG6ARo'  

 
class StdOutListener(StreamListener):
    """ A listener handles tweets that are received from the stream.
    This is a basic listener that just prints received tweets to stdout.
    """
    def on_data(self, data):
        print(data)
        return True

    def on_error(self, status):
        print(status)

if __name__ == '__main__':
    l = StdOutListener()
    auth = OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)

    stream = Stream(auth, l)
    stream.filter(track=['Euro2016'])
