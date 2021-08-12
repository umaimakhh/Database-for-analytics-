

import urllib.request
import json
import time

import sqlite3
conn = sqlite3.connect('dsc450.db') # open the connection
cursor = conn.cursor()

                
#Question 2a
        sqlInsertTweetTablee = """SELECT id_str, AVG(longitude), AVG(latitude) FROM TweetTablee, 
        GEOTable WHERE TweetTablee.id_str = GEOTable.id group by id_str;"""


# Question 2b
def executeQueryNumber(numberofTime):
    for i in range(numberofTime):
        sqlInsertTweetTablee = """SELECT id_str, AVG(longitude), AVG(latitude) FROM TweetTablee, 
        GEOTable WHERE TweetTablee.id_str = GEOTable.id group by id_str;"""
    print("-- Tweet Main table \n\n")
    queryFetchsqlInsertTweetTablee = cursor.execute(sqlInsertTweetTablee).fetchall()
    print(queryFetchsqlInsertTweetTablee)   





startTimeFOR10 = time.time()
executeQueryNumber(10)
endTimeFOR10  = time.time()
TotalTime10 = endTimeFOR10 - startTimeFOR10

startTimeFOR100 = time.time()
executeQueryNumber(100)
endTimeFOR100  = time.time()
TotalTime =  endTimeFOR100 - startTimeFOR100

print("\n Time for 10 time "+str(TotalTime10))
print("Time for 100 time "+str(TotalTime))

conn.commit()
conn.close()

#Question 2c: 

filePath = "E:\DPU\winter 2020\\OneDayTweet600K.txt"
userItemDictionaryLat={}
userItemDictionaryLong={}
webFD = open(filePath,"r")
for i in range(60000):
    tweetLine=webFD.readline()
    try:
        TweetData = json.loads(tweetLine)
        id_str = TweetData.get('id_str')
        if TweetData['geo'] is not None:
            idGeo = TweetData['id']
            geoLatitude = TweetData['geo']['coordinates'][1]
            geoLongitude = TweetData['geo']['coordinates'][0]
            if id_str is not None and idGeo is not None:
                if id_str in userItemDictionaryLat:
                    userItemDictionaryLat[idGeo].append(geoLatitude)
                else:
                    userItemDictionaryLat[idGeo] = [geoLatitude]
                if id_str in userItemDictionaryLong:
                    userItemDictionaryLong[idGeo].append(geoLongitude)
                else:
                    userItemDictionaryLong[idGeo] = [geoLongitude]
    except Exception as e:
        print(str(e))

for userId in userItemDictionaryLat:
    sumofLat = 0
    for lat in userItemDictionaryLat[userId]:
        sumofLat = sumofLat+ lat
    lengthofLat = len(userItemDictionaryLat[userId]) # for average
    print("Average Latitude For user ID "+str(userId) + "-" + str(sumofLat/lengthofLat))

for userId in userItemDictionaryLong:
    sumofLong = 0
    for longi in userItemDictionaryLong[userId]:
        sumofLong = sumofLong + longi
    lengthofLongi = len(userItemDictionaryLong[userId]) # for average
    print("Average Longitiude For user ID "+str(userId) +"-"+str(sumofLong/(lengthofLongi)))


#2d: 
def executeCommandForQuery(numberOfTimes):
    for i in range(numberOfTimes):
        filePath = "E:\DPU\winter 2020\\OneDayTweet600K.txt"
        userItemDictionaryLat={}
        userItemDictionaryLong={}
        webFD = open(filePath,"r")
        for i in range(60000):
            tweetLine=webFD.readline()
            try:
                TweetData = json.loads(tweetLine)
                id_str = TweetData.get('id_str')
                if TweetData['geo'] is not None:
                    idGeo = TweetData['id']
                    geoLatitude = TweetData['geo']['coordinates'][1]
                    geoLongitude = TweetData['geo']['coordinates'][0]
                    if id_str is not None and idGeo is not None:
                        if id_str in userItemDictionaryLat:
                            userItemDictionaryLat[idGeo].append(geoLatitude)
                        else:
                            userItemDictionaryLat[idGeo] = [geoLatitude]
                        if id_str in userItemDictionaryLong:
                            userItemDictionaryLong[idGeo].append(geoLongitude)
                        else:
                            userItemDictionaryLong[idGeo] = [geoLongitude]
            except Exception as e:
                print(str(e))

        for userId in userItemDictionaryLat:
            sumofLat = 0
            for lat in userItemDictionaryLat[userId]:
                sumofLat = sumofLat+ lat
            lengthofLat = len(userItemDictionaryLat[userId]) # for average
            # print("Average Latitude For user ID "+str(userId) + "-" + str(sumofLat/lengthofLat))

        for userId in userItemDictionaryLong:
            sumofLong = 0
            for longi in userItemDictionaryLong[userId]:
                sumofLong = sumofLong + longi
            lengthofLongi = len(userItemDictionaryLong[userId]) # for average
            # print("Average Longitiude For user ID "+str(userId) +"-"+str(sumofLong/(lengthofLongi)))


startTimeFOR10 = time.time()
executeCommandForQuery(10)
endTimeFOR10  = time.time()
TotalTime10 = endTimeFOR10 - startTimeFOR10

startTimeFOR100 = time.time()
executeCommandForQuery(100)
endTimeFOR100  = time.time()
TotalTime =  endTimeFOR100 - startTimeFOR100

print("\n Time for 10 time for 2d "+str(TotalTime10))
print("Time for 100 time for 2d "+str(TotalTime))


# Question 2e
import re
filePath = "E:\DPU\winter 2020\\OneDayTweet600K.txt"
webFD = open(filePath,"r")
    queryResult = []   
for i in range(60000):
    tweetLine=webFD.readline()
    try:
        
            p =  (re.findall(r'"id":(\w+)', tweetLine))

            coordinates = (re.findall(r'"coordinates":(.\d(?:[,\d]*\.\d+|[,\d]*))', tweetLine)) 
            queryResult.append(p)
            queryResult.append(coordinates)
            # if coordinates is not None: #show only those users with lat long
            #     print(p)
            #     print(coordinates)
            #     print("\n")
        
    except Exception as e:
        print(str(e))


#Question 2f
import re
def exceuteRegex(numberOfTimes): 
    queryResult = []   
    filePath = "E:\DPU\winter 2020\\OneDayTweet600K.txt"
    webFD = open(filePath,"r")
    for i in range(60000):
        tweetLine=webFD.readline()
        try:
            
            p =  (re.findall(r'"id":(\w+)', tweetLine))

            coordinates = (re.findall(r'"coordinates":(.\d(?:[,\d]*\.\d+|[,\d]*))', tweetLine)) 
            queryResult.append(p)
            queryResult.append(coordinates)
            # if coordinates is not None: #show only those users with lat long
                # print(p)
                # print(coordinates)
                # print("\n")
            
        except Exception as e:
            print(str(e))

startTimeFOR10 = time.time()
exceuteRegex(10)
endTimeFOR10  = time.time()
TotalTime10 = endTimeFOR10 - startTimeFOR10

startTimeFOR100 = time.time()
exceuteRegex(100)
endTimeFOR100  = time.time()
TotalTime =  endTimeFOR100 - startTimeFOR100

print("\n Time for 10 time for 2 F "+str(TotalTime10))
print("Time for 100 time for 2 F "+str(TotalTime))


