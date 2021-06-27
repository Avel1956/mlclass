import tweepy
import pandas as pd
import os
import csv
import datetime
import json
import time


def open_csv (filename):
#Esta funcion tiene como entrada el nombre de un archivo en el workpath con formato 
#.csv y devuelve un dataframe con los contenidos del archivo con los 
#contenidos de la primera fila como encabezados.
    df = pd.read_csv (filename)
    return df

df = open_csv("api_ref.csv")
key = df['key'][1]
secret = df['secret'][1]
ac_tok = df['access token'][1]
ac_sec = df['access secret'][1]
#########################################


#Add your credentials here
twitter_keys = {
        'consumer_key':        key,
        'consumer_secret':   secret,
        'access_token_key':    ac_tok,
        'access_token_secret': ac_sec
    }

#Setup access to API
auth = tweepy.OAuthHandler(twitter_keys['consumer_key'], twitter_keys['consumer_secret'])
auth.set_access_token(twitter_keys['access_token_key'], twitter_keys['access_token_secret'])

api = tweepy.API(auth)

#Make call on home timeline, print each tweets text
#public_tweets = api.home_timeline()
#for tweet in public_tweets:
#    print(tweet.text)

user = api.get_user('javelezea')

print(user.screen_name)
print(user.followers_count)
for tweet in user():
   print(tweet.text)






