import psycopg2
import pandas as pd
import os
pwd = "root"


def createOrUpdateTransaction(transId:int,TransName,TransType,TransStatus):
    conn = psycopg2.connect(user="postgres",password=pwd,dbname="python_tutorial")
    stmt = None
    if "created" == TransStatus.lower():
        print("Calling insert")
        stmt =  f" INSERT INTO TRANSACTION (TRANS_ID,TRANS_NAME,TRANS_STATUS,TransType) VALUES({transId},'{TransName}','{TransStatus}','{TransType}')"
    else:
        print("Calling update")
        stmt = f"UPDATE TRANSACTION SET TRANS_STATUS = '{TransStatus}' WHERE TRANS_ID={transId}"
    conn.cursor().execute(stmt)
    conn.commit()
    conn.close()

    
    


