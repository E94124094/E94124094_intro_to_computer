# 客家委員會桐花景點步道
# https://data.gov.tw/dataset/166163

import pymysql.cursors
import requests
import json

#GET API data
test = requests.get("https://cloud.hakka.gov.tw/Pub/Opendata/DTST20231000005.json")
r = json.loads(test.text)

#Connect to the database
try:
    connection = pymysql.connect(host='localhost',  # 我的伺服器/主機
                                 user='E94124094',       # 我資料庫的帳號
                                 password='0000', # 我資料庫的密碼
                                 database='wordpress',     # 我資料庫的名稱
                                 cursorclass=pymysql.cursors.DictCursor)
    print("連線成功")     
except Exception as error: # 出現意外時印出
    print(error)


with connection:
    with connection.cursor() as cursor:

        # SQL語法不會考
        sql = "INSERT INTO `客家委員會桐花景點步道` (`SEQNO`, `viewpoint`, `address`, `LocalCallService`) VALUES (%s, %s, %s, %s)"
        for i in range( len( r ) ):
            cursor.execute(sql, (r[i]['SEQNO'],r[i]['viewpoint'],r[i]['address'],r[i]['LocalCallService']))

    connection.commit()
    cursor.close()
