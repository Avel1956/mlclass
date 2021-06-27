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


key = df['key'][0]
secret = df['secret'][0]


def initiate_api():

    try: 

            

        auth = tweepy.OAuthHandler(key, secret)

        

        api = tweepy.API(auth)

        return api

    except:

        print("Problems with config.json")

        return None
def get_tweets(api, query):

    tweets = []

    for status in tweepy.Cursor(api.search,

                       q=query,

                       count=1000,

                       result_type='popular',

                       include_entities=True,

                       monitor_rate_limit=True, 

                       wait_on_rate_limit=True,

                       lang="es").items():

     

        # Getting only tweets which has english dialects

        if isEspanish(status.text) == True:

            tweets.append([status.id_str, query, status.created_at.strftime('%d-%m-%Y %H:%M'), status.user.screen_name, status.text])

    return tweets
#api = tweepy.API(auth)
#cursor = tweepy.Cursor(api.search, q = "machine learning", tweet_mode = "extended").items(1)
#for i in cursor:
#    print (i.full_text)
def get_woeid(api, locations):

    twitter_world = api.trends_available()

    places = {loc['name'].lower() : loc['woeid'] for loc in twitter_world};

    woeids = []

    for location in locations:

        if location in places:

            woeids.append(places[location])

        else:

            print("err: ",location," woeid does not exist in trending topics")

    return woeids

def get_trending_hashtags(api, location):

    woeids = get_woeid(api, location)

    trending = set()

    for woeid in woeids:

        try:

            trends = api.trends_place(woeid)

        except:

            print("API limit exceeded. Waiting for next hour")

            #time.sleep(3605) # change to 5 for testing

            trends = api.trends_place(woeid)

        # Checking for English dialect Hashtags and storing text without #

        topics = [trend['name'][1:] for trend in trends[0]['trends'] if (trend['name'].find('#') == 0 and isEspanish(trend['name']) == True)]

        trending.update(topics)

    

    return trending

def twitter_bot(api, locations):

    today = datetime.datetime.today().strftime("%d-%m-%Y-%H-%M%S")

    if not os.path.exists("trending_tweets"):

        os.makedirs("trending_tweets")

    file_tweets = open("trending_tweets/"+today+"-tweets.csv", "a+")

    file_hashtags = open("trending_tweets/"+today+"-hashtags.csv", "w+")

    writer = csv.writer(file_tweets)

    

    hashtags = get_trending_hashtags(api, locations)

    file_hashtags.write("\n".join(hashtags))

    print("Hashtags written to file.")

    file_hashtags.close()

    

    for hashtag in hashtags:

        try:

            print("Getting Tweets for the hashtag: ", hashtag)

            tweets = get_tweets(api, "#"+hashtag)

        except:

            print("API limit exceeded. Waiting for next hour")

            #time.sleep(3605) # change to 0.2 sec for testing

            tweets = get_tweets(api, "#"+hashtag)

        for tweet in tweets:

            writer.writerow(tweet)

    

    file_tweets.close()

def isEspanish(text):

    try:

        text.encode(encoding='utf-8').decode('ascii')

    except UnicodeDecodeError:

        return False

    else:

        return True

location = ['colombia']
api = initiate_api()

twitter_bot(api, location)