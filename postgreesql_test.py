import psycopg2
import pandas as pd
import os
from dotenv import load_dotenv


load_dotenv()

pwd = os.environ['DB_PWD']

print(pwd)

conn = psycopg2.connect(user="postgres",password=pwd,dbname="python_tutorial"
                        
)

curr = conn.cursor()

curr.execute("SELECT * FROM EMP")

rows = curr.fetchall()

conn.commit()
conn.close()

df =  pd.DataFrame(rows,columns=["id","Name"])

print(df)


