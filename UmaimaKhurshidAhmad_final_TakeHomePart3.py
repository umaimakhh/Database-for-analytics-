import urllib.request
import json
import time

import sqlite3
conn = sqlite3.connect('dsc450.db') # open the connection
cursor = conn.cursor()
sqlInsertTweetTablee = """SELECT *
FROM TweetTablee
LEFT OUTER JOIN user_Dictionaryy
ON TweetTablee.id_str = user_Dictionaryy.id 
UNION 
SELECT *
FROM GEOTable
LEFT OUTER JOIN TweetTablee
ON TweetTablee.id_str = GEOTable.id
"""

queryFetchsqlInsertTweetTablee = cursor.execute(sqlInsertTweetTablee).fetchall()
# print(queryFetchsqlInsertTweetTablee)   
print('Successful 3a')

# #3b:
outputPathForJason = "E:\DPU\winter 2020\\3bjsonFinal_umaima.txt"
jsonDump = json.dumps(queryFetchsqlInsertTweetTablee)
outputFile= open(outputPathForJason,"w+")
outputFile.write((jsonDump))
outputFile.close()
print('Json Format saved successfully in '+ outputPathForJason)

#3c
import csv
outputPathForCsv = "E:\DPU\winter 2020\\3cjsonFileFinal_umaima.csv"
with open(outputPathForCsv, 'w',encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerows(queryFetchsqlInsertTweetTablee)
print('CSV Format saved successfully in '+ outputPathForCsv)


