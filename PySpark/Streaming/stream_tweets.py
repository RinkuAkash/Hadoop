import json
import tweepy
import socket

access_token = '1704496008-q7TrrEaLPFPC2DJwXl9vconm2MODvzY8G9Ey2Tw'
access_secret = 'DvMlLi2vfkD6SoQKNW677GSwteNMPRMNRwel38mMsO71z'
consumer_key = 'TCUomnQOppUnygMBFavmYaVqG'
consumer_secret = '1Xts4khf3lXQrYDIAxUwUr7clJw5XogFBcc5Uxh5fCQtk2SYSE'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

class TweetsListener(tweepy.StreamListener):
    def __init__(self, csocket):
        self.client_socket = csocket

    def on_data(self, data):
        try:
            message = json.loads(data)
            print(message['text'])
            self.client_socket.send(str(message['text']+"\n").encode('utf-8'))
            return True
        except BaseException as e:
            print("Error on_data %s" %str(e))
            return True

    def on_error(self, status):
        print(status)
        return True

def sendData(c_socket):
    stream = tweepy.Stream(auth, TweetsListener(c_socket))
    stream.filter(track=['hadoop', 'data science', 'spark', 'big data', 'pyspark'], languages=['en'])

if __name__=="__main__":
    s = socket.socket()
    host = "127.0.0.1"
    port = 9000
    s.bind((host, port))
    print("Listening on port: %s" %str(port))
    s.listen(5)
    c, addr = s.accept()
    print("Received request from: " +str(addr))
    sendData(c)

