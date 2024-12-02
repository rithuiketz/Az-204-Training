from hashlib import sha256
from sqlalchemy import create_engine
from sqlalchemy.orm import Session,sessionmaker
from sqlalchemy import URL
from qcomm_usermgmt.src.orm.Entity import User,UserCommunications,UserAuth
from sqlalchemy import select
import os


class DBService():

    def __init__(self):
        dbHost = os.getenv("DB_HOST","database-1.cvqgcygm0awc.ap-south-1.rds.amazonaws.com")
        print("DB HOST "+dbHost)
        self.url = URL.create("postgresql+psycopg2",username="postgres",password="root",host=dbHost,database="postgresdb1",port="5432")
        self.engine = engine = create_engine(self.url)
    
    def persist_obj(self,obj):
        with Session(self.engine) as session:
            session.add(obj)
            session.commit()
    
    def get_user_by_login(self,login):
        data ={}
        with Session(self.engine) as session:
            data = session.execute(select(UserAuth).where(UserAuth.login==login)).first()
            print(data)
            
        return data


        
