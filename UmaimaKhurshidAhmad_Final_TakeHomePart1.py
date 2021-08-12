# urlLink = "http://rasinsrv07.cstcis.cti.depaul.edu/CSC455/OneDayOfTweets.txt"
# import urllib.request as urllib
# import time
# import matplotlib.pyplot as plt
# #a 50,000 tweets, 200,000 tweets, and 600,000 tweets. 
# outfile50K= open("E:\DPU\winter 2020\\OneDayTweet50K.txt","w+")
# outfile200K= open("E:\DPU\winter 2020\\OneDayTweet200K.txt","w+")
# outfile600K= open("E:\DPU\winter 2020\\OneDayTweet600K.txt","w+")

# dataFromURL  = urllib.urlopen(urlLink)


# def outTweetsInFile(numberOfTweets,outputFile):
#     for data in range(numberOfTweets):
#         try:
#             response = dataFromURL.readline().decode("utf8")   
#             outputFile.write((response))
#         except ValueError:
#             None

#part 1b
#b.	For each string (CHAR OR VARCHAR) column in your 3-table schema,
#  find the length of the longest string in the file in 1-a and compare it to your data type size. 
# You only need to do 1-b for 500,000 tweets. 

import json
import time
import sqlite3

#from homework 9 Geo table 3rd table schema
createtblTweetTable  = """CREATE TABLE TweetTablee -- creating Employee Job table
(
  created_at DATE,
  id_str VARCHAR2(20),
  text VARCHAR2(50),
  source VARCHAR2(100),
  in_reply_to_user_id NUMBER(20),
  in_reply_to_screen_name VARCHAR2(15),
  in_reply_to_status_id NUMBER(20),
  retweet_count NUMBER(5),
  contributors VARCHAR2(10),
  user_id NUMBER(7),
  
  CONSTRAINT id_PK
     PRIMARY KEY(id_str)
);"""

createGEOTable = """CREATE TABLE GEOTable -- creating GEO Job table
(
  
  id VARCHAR2(20),
  type VARCHAR2(50),
  longitude VARCHAR2(100),
  latitude VARCHAR2(100),
  
  CONSTRAINT id
     PRIMARY KEY(id)
);"""

createtbleUserDicTable  = """CREATE TABLE user_Dictionaryy -- creating Employee Job table
(
  id NUMBER(7),
  name VARCHAR2(50),
  screen_name VARCHAR2(100),
  friends_count NUMBER(20),
  
  CONSTRAINT id_PK
     PRIMARY KEY(id)


);"""

id_SIZE_GEO_TABLE = 20
type_SIZE_GEO_TABLE = 50
longitude_SIZE_GEO_TABLE = 100
latitude_SIZE_GEO_TABLE = 100

id_str_SIZE_TWEET_TABLE = 20
text_SIZE_TWEET_TABLE = 50
source_SIZE_TWEET_TABLE = 100
in_reply_to_screen_name_SIZE_TWEET_TABLE = 15
contributors_SIZE_TWEET_TABLE = 15

name_SIZE_USER_DICTIONARY_TABLE = 50
screen_name_SIZE_USER_DICTIONARY_TABLE = 100


file = open("E:\DPU\winter 2020\\OneDayTweet600K.txt","r")
tweetLine = file.readlines()

#inital length of all varibales is 0
#--geo table

perviousLengthId = 0
perviousLengthgeotype = 0
perviousLengthgeoLongitude = 0 
perviousLengthgeoLatitude = 0

#-- tweet table 
perviousLengthcreatedAt = 0
perviousLengthgeoid_str = 0
perviousLengthtext = 0 
perviousLengthsource = 0
perviousLengthInnReplyTweetName = 0
perviousLengthcontributors = 0

#-- user dictionary table
perviousLengthname = 0
perviousLengthscreen_name = 0 

for tweet in tweetLine:
    try:

        TweetData = json.loads(tweet) # load json
        
        createdAt = TweetData.get('created_at')
        if len(str(createdAt)) > perviousLengthcreatedAt:
            perviousLengthcreatedAt = len(str(createdAt)) 


        id_str = TweetData.get('id_str')
        if len(str(id_str)) > perviousLengthgeoid_str:
            perviousLengthgeoid_str = len(str(id_str)) 


        text = TweetData.get('text')
        if len(str(text)) > perviousLengthtext:
            perviousLengthtext = len(str(text)) 


        source = TweetData.get('source')
        if len(str(source)) > perviousLengthsource:
            perviousLengthsource = len(str(source)) 
        
        in_reply_to_screen_name = TweetData.get('in_reply_to_screen_name')
        if len(str(in_reply_to_screen_name)) > perviousLengthInnReplyTweetName:
            perviousLengthInnReplyTweetName = len(str(in_reply_to_screen_name)) 


        contributors = TweetData.get('contributors')
        if len(str(contributors)) > perviousLengthcontributors:
            perviousLengthcontributors = len(str(contributors)) 



        name = TweetData['user']['name']
        if len(str(name)) > perviousLengthname:
            perviousLengthname = len(str(name))

        

        screen_name = TweetData['user']['screen_name']
        if len(str(screen_name)) > perviousLengthscreen_name:
            perviousLengthscreen_name = len(str(name))


        idGeo = TweetData['id']
        if len(str(idGeo)) > perviousLengthId:
            perviousLengthId = len(str(idGeo)) 

        if TweetData['geo'] is not None:
            geotype = TweetData['geo']['type']
            if len(str(geotype)) > perviousLengthgeotype:
                perviousLengthgeotype = len(str(geotype)) 

            geoLatitude = TweetData['geo']['coordinates'][1]
            if len(str(geoLatitude)) > perviousLengthgeoLatitude:
                perviousLengthgeoLatitude = len(str(geoLatitude)) 
            

            geoLongitude = TweetData['geo']['coordinates'][0]
            if len(str(geoLongitude)) > perviousLengthgeoLongitude:
                perviousLengthgeoLongitude = len(str(geoLongitude))
    except ValueError:
        None 

print("The higest Size of ID from file is " + str(perviousLengthId) + " and Size of GEO table scehme is" +str(id_SIZE_GEO_TABLE))
print("\n The higest Size of TYPE from file is " + str(perviousLengthgeotype) + " and Size of GEO table scehme is" +str(type_SIZE_GEO_TABLE))
print("\n The higest Size of ID from file is " + str(perviousLengthgeoLatitude) + " and Size of GEO table scehme is" +str(latitude_SIZE_GEO_TABLE))
print("\nThe higest Size of ID from file is " + str(perviousLengthgeoLongitude) + " and Size of GEO table scehme is" +str(longitude_SIZE_GEO_TABLE))

print("\n\n\nThe higest Size of created at from file is " + str(perviousLengthcreatedAt) + " and Size of GEO table scehme is" +str(id_str_SIZE_TWEET_TABLE))
print("\n The higest Size of TYPE from file is " + str(perviousLengthgeoid_str) + " and Size of GEO table scehme is" +str(id_str_SIZE_TWEET_TABLE))
print("\n The higest Size of ID from file is " + str(perviousLengthtext) + " and Size of GEO table scehme is" +str(text_SIZE_TWEET_TABLE))
print("\nThe higest Size of ID from file is " + str(perviousLengthsource) + " and Size of GEO table scehme is" +str(source_SIZE_TWEET_TABLE))
print("\n The higest Size of ID from file is " + str(perviousLengthInnReplyTweetName) + " and Size of GEO table scehme is" +str(source_SIZE_TWEET_TABLE))
print("\nThe higest Size of ID from file is " + str(perviousLengthcontributors) + " and Size of GEO table scehme is" +str(contributors_SIZE_TWEET_TABLE)) 


name_SIZE_USER_DICTIONARY_TABLE = 50
screen_name_SIZE_USER_DICTIONARY_TABLE = 100

print("\n\n\nThe higest Size of created at from file is " + str(perviousLengthname) + " and Size of GEO table scehme is" +str(name_SIZE_USER_DICTIONARY_TABLE))
print("\n The higest Size of TYPE from file is " + str(perviousLengthscreen_name) + " and Size of GEO table scehme is" +str(screen_name_SIZE_USER_DICTIONARY_TABLE))



# #Part 1e
# startTimeFor50K = time.time()
# outTweetsInFile(50000,outfile50K)
# endTimeFor50K = time.time()

# startTimeFor200K = time.time()
# outTweetsInFile(200000,outfile200K)
# endTimeFor200K = time.time()

# startTimeFor600K = time.time()
# outTweetsInFile(600000,outfile600K)
# endTimeFor600K = time.time()
# TimeFor500 = endTimeFor50K - startTimeFor50K 
# TimeFor200 = endTimeFor200K - startTimeFor200K 
# TimeFor600 = endTimeFor600K - startTimeFor600K 

# outfile50K.close()
# outfile200K.close()
# outfile600K.close()

# import numpy as np 
# x = np.array([50000, 200000,600000]) 
# y = np.array([TimeFor500, TimeFor200,TimeFor600]) 
# plt.plot(x,y,marker = 'o', ms = 15)
# plt.title("Line Graph for the analysis of tweets runtime - Part 1 a")
# plt.xlabel("Number of Tweets")
# plt.ylabel("Time in seconds")
# plt.show()

