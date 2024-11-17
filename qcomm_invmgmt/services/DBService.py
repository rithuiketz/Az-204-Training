from hashlib import sha256
from sqlalchemy import create_engine
from sqlalchemy.orm import Session,sessionmaker
from sqlalchemy import URL
from orm.Entity import User,UserCommunications,UserAuth
from sqlalchemy import select


class DBService():

    def __init__(self):
        self.url = URL.create("postgresql+psycopg2",username="postgres",password="Welcome@1234",host="localhost",database="postgres",port="5432")
        self.engine = engine = create_engine(self.url)
    
    def persist_obj(self,obj):
        with Session(self.engine) as session:
            session.add(obj)
            session.commit()


        
