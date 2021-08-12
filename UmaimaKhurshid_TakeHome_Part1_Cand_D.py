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

#writing tweet data from url 

import urllib.request
import json
import time

import sqlite3
conn = sqlite3.connect('dsc450.db') # open the connection
cursor = conn.cursor()
cursor.execute('DROP TABLE IF EXISTS TweetTablee') 
cursor.execute('DROP TABLE IF EXISTS user_Dictionaryy')  
cursor.execute('DROP TABLE IF EXISTS GEOTable')  
cursor.execute(createtbleUserDicTable)
cursor.execute(createtblTweetTable)
cursor.execute(createGEOTable)
def populateLinkForTweetData(isPopulateFromFile,fileNumber):
    '''returns the file path of one of the three files made in part 1 a, or the path of the web based on the
    true or false value given by the user
    
    input patameters:
    fileNumber = 50000 for 50000 tweets, 100000TweetFile for 100000 tweets, 500000TweetFile for 500000 tweets'''
    if isPopulateFromFile:
        if fileNumber == "50000TweetFile":
            filePath = "E:\DPU\winter 2020\\OneDayTweet50K.txt"
        elif fileNumber == "200000TweetFile":
            filePath = "E:\DPU\winter 2020\\OneDayTweet200K.txt"
        elif fileNumber == "600000TweetFile":
            filePath = "E:\DPU\winter 2020\\OneDayTweet600K.txt"
    else:
        filePath = "http://rasinsrv07.cstcis.cti.depaul.edu/CSC455/OneDayOfTweets.txt"
    return filePath





def populateRange(rangeNumber,isPopulateFromFile,filePath):
    '''gives the populated range'''
    if isPopulateFromFile is not True:
        webFD = urllib.request.urlopen(filePath)
    else:
        webFD = open(filePath,"r")

    for i in range(rangeNumber):
        tweetLine=webFD.readline()
        try:
            insertQueryTweetTable = 'INSERT OR IGNORE INTO TweetTablee VALUES (?,?,?,?,?,?,?,?,?,?);'  
            insertQueryUserDic = 'INSERT OR IGNORE INTO user_Dictionaryy VALUES (?,?,?,?);'
            insertQueryGeoTable = 'INSERT OR IGNORE INTO GEOTable VALUES (?,?,?,?);'  

            dataEntryTweetTable1 = []
            dataEntryUserDictionary = []
            dataEntryGeoTable = []

            TweetData = json.loads(tweetLine) # load json
            createdAt = TweetData.get('created_at')
            dataEntryTweetTable1.append(createdAt) # load cols to list

            id_str = TweetData.get('id_str')
            dataEntryTweetTable1.append(id_str)

            text = TweetData.get('text')
            dataEntryTweetTable1.append(text)

            source = TweetData.get('source')
            dataEntryTweetTable1.append(source)

            in_reply_to_user_id = TweetData.get('in_reply_to_user_id')
            dataEntryTweetTable1.append(in_reply_to_user_id)

            in_reply_to_screen_name = TweetData.get('in_reply_to_screen_name')
            dataEntryTweetTable1.append(in_reply_to_screen_name)

            in_reply_to_status_id = TweetData.get('in_reply_to_status_id')
            dataEntryTweetTable1.append(in_reply_to_status_id)

            retweet_count = TweetData.get('retweet_count')
            dataEntryTweetTable1.append(retweet_count)

            contributors = TweetData.get('contributors')
            dataEntryTweetTable1.append(contributors)
            
            

            id = TweetData['user']['id']
            dataEntryUserDictionary.append(id)
            dataEntryTweetTable1.append(id)


            name = TweetData['user']['name']
            dataEntryUserDictionary.append(name) 
            

            screen_name = TweetData['user']['screen_name']
            dataEntryUserDictionary.append(screen_name)

            friends_count = TweetData['user']['friends_count']
            dataEntryUserDictionary.append(friends_count)  
            # dataEntryUserDictionary.append(user_id)


            idGeo = TweetData['id']
            dataEntryGeoTable.append(idGeo) 
            if TweetData['geo'] is not None:
                geotype = TweetData['geo']['type']
                dataEntryGeoTable.append(geotype) 

                geoLatitude = TweetData['geo']['coordinates'][1]
                dataEntryGeoTable.append(geoLatitude) 
                geoLongitude = TweetData['geo']['coordinates'][0]
                dataEntryGeoTable.append(geoLongitude)
                conn.execute(insertQueryGeoTable,dataEntryGeoTable)


            conn.execute(insertQueryTweetTable,dataEntryTweetTable1)
            conn.execute(insertQueryUserDic,dataEntryUserDictionary)

        except Exception:
            None

isPopulateFromFile = True #MAKE TRUE IF POPULATE FROM FILE

#
startTimeFor600K = time.time()
populateRange(600000,isPopulateFromFile,populateLinkForTweetData(isPopulateFromFile,"600000TweetFile"))
endTimeFor600K = time.time()

#populate from file 
isPopulateFromFile = False #MAKE TRUE IF POPULATE FROM FILE
startTimeFromWeb50K = time.time()
populateRange(50000,isPopulateFromFile,populateLinkForTweetData(isPopulateFromFile,""))
endTimeFromWeb50K  = time.time()

startTimeFromWeb200K = time.time()
populateRange(200000,isPopulateFromFile,populateLinkForTweetData(isPopulateFromFile,""))
endTimeFromWeb200K  = time.time()

startTimeFromWeb600K = time.time()
populateRange(600000,isPopulateFromFile,populateLinkForTweetData(isPopulateFromFile,""))
endTimeFromWeb600K  = time.time()

#time calculation from web link
TimeFor500 = endTimeFromWeb50K - startTimeFromWeb50K 
TimeFor200 = endTimeFromWeb200K - startTimeFromWeb200K 
TimeFor600 = endTimeFromWeb600K - startTimeFromWeb600K 


#time calculation from file
TimeForFile500 = endTimeFor50K - startTimeFor50K 
TimeForFile200 = endTimeFor200K - startTimeFor200K 
TimeForFile600 = endTimeFor600K - startTimeFor600K 

#for part 1e
import numpy as np 
import matplotlib.pyplot as plt
  
x = np.array([50000, 200000,600000]) 
y = np.array([TimeForFile500, TimeForFile200,TimeForFile600]) 
plt.plot(x,y,marker = 'o', ms = 15,label = "Data from file Part 1 - d") #plot from data from file
plt.title("Line Graph for the analysis of tweets runtime - Part 1 d")
plt.xlabel("Number of Tweets")
plt.ylabel("Time in seconds")



v = np.array([50000, 200000,600000]) 
z= np.array([TimeFor500, TimeFor200,TimeFor600]) 
plt.plot(v,z,marker = 'o', ms = 15,label = "Data from web Part 1- c") # data from web

plt.show()

#verifiy data sucessfully loaded

sqlInsertTweetTablee = """select COUNT(*) from TweetTablee;"""
queryFetchsqlInsertTweetTablee = cursor.execute(sqlInsertTweetTablee).fetchall()



sqlInsertuser_Dictionaryy = """select COUNT(*) from user_Dictionaryy;"""
queryFetchsqluser_Dictionaryy = cursor.execute(sqlInsertuser_Dictionaryy).fetchall()



sqlInsertGEOTable = """select COUNT(*) from GEOTable;"""
queryFetchsqlGEOTable = cursor.execute(sqlInsertGEOTable).fetchall()


print("Count of Rows in Tweet Table "+str(queryFetchsqlInsertTweetTablee))
print("Count of Rows in User Dictionary Table "+str(queryFetchsqluser_Dictionaryy))
print("Count of Rows in GEO Table "+str(queryFetchsqlGEOTable))


# print("-- Tweet Main table \n\n")
# print(queryFetchsqlInsertTweetTablee)
# print("-- User Dictionary Table Main table \n\n")
# print(queryFetchsqluser_Dictionaryy)
# print("-- Geo Table Main table \n\n")
# print(queryFetchsqlGEOTable)

conn.commit()
conn.close()






