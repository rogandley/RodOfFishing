#!/usr/bin/env python
# -*- coding: utf-8 -*-

import tweepy, time, random, os
from boto.s3.connection import S3Connection

#enter the corresponding information from your Twitter application:
#CONSUMER_KEY = keys.consumerK#keep the quotes, replace this with your consumer key
#CONSUMER_SECRET = keys.consumerS#keep the quotes, replace this with your consumer secret key
#ACCESS_KEY = keys.accessK#keep the quotes, replace this with your access token
#ACCESS_SECRET = keys.accessS#keep the quotes, replace this with your access token secret
auth = tweepy.OAuthHandler(os.environ['CONSUMER_KEY'], os.environ['CONSUMER_SECRET'])
auth.set_access_token(os.environ['ACCESS_KEY'], os.environ['ACCESS_SECRET'])
api = tweepy.API(auth)
lastImg = ''

while(True):
    value = random.random()
    if(value > .9):
        filename = "Resources/missedlines.txt"
        image = "Resources/Red_Onion.png"
        line = random.choice([line for line in open(filename)])
    elif(value > .87):
        filename = 'Resources/Chaos'
        fish = filename + "/" + random.choice(os.listdir(filename))
        for file in os.listdir(fish):
            if file.endswith(".txt"):
                lines = fish + "/" + file
            else:
                image = fish + "/" + file
        line = random.choice([line for line in open(lines)])
    elif(value > .75):
        filename = 'Resources/Styx'
        fish = filename + "/" + random.choice(os.listdir(filename))
        for file in os.listdir(fish):
            if file.endswith(".txt"):
                lines = fish + "/" + file
            else:
                image = fish + "/" + file
        line = random.choice([line for line in open(lines)])
    elif(value > .525):
        filename = 'Resources/Elysium'
        fish = filename + "/" + random.choice(os.listdir(filename))
        for file in os.listdir(fish):
            if file.endswith(".txt"):
                lines = fish + "/" + file
            else:
                image = fish + "/" + file
        line = random.choice([line for line in open(lines)])
    elif(value > .275):
        filename = 'Resources/Asphodel'
        fish = filename + "/" + random.choice(os.listdir(filename))
        for file in os.listdir(fish):
            if file.endswith(".txt"):
                lines = fish + "/" + file
            else:
                image = fish + "/" + file
        line = random.choice([line for line in open(lines)])
    else:
        filename = 'Resources/Tartarus'
        fish = filename + "/" + random.choice(os.listdir(filename))
        for file in os.listdir(fish):
            if file.endswith(".txt"):
                lines = fish + "/" + file
            else:
                image = fish + "/" + file
        line = random.choice([line for line in open(lines)])

    if(lastImg == image):
        continue

    api.update_with_media(image, line)
    lastImg = image

    time.sleep(3600)