import pymysql
import os



def connect_to_database():
    hostname= '127.0.0.1'
    user ='root'
    password = '9832553619@@mIIRSHE'
    database= 'my_database'
    
    connection=pymysql.connect(host=hostname,user=user,password=password,database=database)
    
    return connection,connection.cursor(prepared=True)



def insert(query:str,params:list):
    conn,cursor=connect_to_database()
    cursor.execute(query,params)
    conn.commit()
    print("Data Inserted successully into the table")
    
    
    

def fetch(query:str,params):
    conn,cursor=connect_to_database()
    cursor.execute(query,params)
    result=cursor.fetchall()
    return result


def close_connection():
    conn,cursor=connect_to_database()
    cursor.close()
    conn.close()
    
    
