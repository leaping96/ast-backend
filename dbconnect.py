
import pymysql

def db_con():
    db = pymysql.connect(
            host='127.0.0.1', 
            port=3306, 
            user='root', 
            passwd='123123', 
            db='ast', 
            charset='utf8'
        
        )
    return db