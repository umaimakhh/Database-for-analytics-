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
        elif fileNumber == "100000TweetFile":
            filePath = "E:\DPU\winter 2020\\OneDayTweet100K.txt"
        elif fileNumber == "500000TweetFile":
            filePath = "E:\DPU\winter 2020\\OneDayTweet2500K.txt"
    else:
        filePath = "http://rasinsrv07.cstcis.cti.depaul.edu/CSC455/OneDayOfTweets.txt"
    return filePath





def populateRange(rangeNumber,isPopulateFromFile,filePath):
    '''gives the populated range'''

    batchSizee = 1000
    if isPopulateFromFile is not True:
        webFD = urllib.request.urlopen(filePath)
    else:
        webFD = open(filePath,"r")

    BatchdataEntryTweetTable1 = []
    BatchdataEntryUserDictionary = []
    BatchdataEntryGeoTable = []


    for i in range(rangeNumber):
        tweetLine=webFD.readline().decode("utf-8") 
        dataEntryTweetTable1 = []
        dataEntryUserDictionary = []
        dataEntryGeoTable = []
        try:
            insertQueryTweetTable = 'INSERT OR IGNORE INTO TweetTablee VALUES (?,?,?,?,?,?,?,?,?,?);'  
            insertQueryUserDic = 'INSERT OR IGNORE INTO user_Dictionaryy VALUES (?,?,?,?);'
            insertQueryGeoTable = 'INSERT OR IGNORE INTO GEOTable VALUES (?,?,?,?);'  


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
                BatchdataEntryGeoTable.append(tuple(dataEntryGeoTable))
                dataEntryGeoTable= []
                
                if len(BatchdataEntryGeoTable) == batchSizee:
                    conn.executemany(insertQueryGeoTable,BatchdataEntryGeoTable)
                    BatchdataEntryGeoTable = [] #empty list for next batch

            BatchdataEntryTweetTable1.append(tuple(dataEntryTweetTable1))
            dataEntryTweetTable1 = []
            BatchdataEntryUserDictionary.append(tuple(dataEntryUserDictionary))
            dataEntryUserDictionary = []
            if len(BatchdataEntryTweetTable1) == batchSizee:
                conn.executemany(insertQueryTweetTable,BatchdataEntryTweetTable1)
                BatchdataEntryTweetTable1 = [] # empty list for next batch
            if len(BatchdataEntryUserDictionary) == batchSizee:
                conn.executemany(insertQueryUserDic,BatchdataEntryUserDictionary)
                BatchdataEntryUserDictionary = []
            

        except Exception as e:
            print(str(e))
                    

isPopulateFromFile = False #MAKE TRUE IF POPULATE FROM FILE

#populate for 50000,100,000 and 500,000
populateRange(50000,isPopulateFromFile,populateLinkForTweetData(isPopulateFromFile,"50000TweetFile"))
# populateRange(100000,isPopulateFromFile,populateRange(isPopulateFromFile,100000))
# populateRange(500000,isPopulateFromFile,populateRange(isPopulateFromFile,500000))

sqlInsertTweetTablee = """select * from TweetTablee LIMIT 10;"""
sqlInsertuser_Dictionaryy = """select * from user_Dictionaryy LIMIT 10;"""
sqlInsertGEOTable = """select * from GEOTable LIMIT 10;"""
queryFetchsqlInsertTweetTablee = cursor.execute(sqlInsertTweetTablee).fetchall()
queryFetchsqluser_Dictionaryy = cursor.execute(sqlInsertuser_Dictionaryy).fetchall()
queryFetchsqlGEOTable = cursor.execute(sqlInsertGEOTable).fetchall()

print("-- Tweet Main table \n\n")
print(queryFetchsqlInsertTweetTablee)
print("-- User Dictionary Table Main table \n\n")
print(queryFetchsqluser_Dictionaryy)
print("-- Geo Table Main table \n\n")
print(queryFetchsqlGEOTable)

conn.commit()
conn.close()






