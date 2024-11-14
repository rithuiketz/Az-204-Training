from hashlib import sha256
from sqlalchemy import create_engine
from sqlalchemy.orm import Session,sessionmaker
from sqlalchemy import URL
from orm.Entity import User,UserCommunications,UserAuth
from sqlalchemy import select


class DBService():

    def __init__(self):
        self.url = URL.create("postgresql+psycopg2",username="postgres",password="root",host="localhost",database="postgres",port="5432")
        self.engine = engine = create_engine(self.url)
    
    def persist_obj(self,obj):
        with Session(self.engine) as session:
            session.add(obj)
            session.commit()
    
    def get_user_by_login(self,login):
        data ={}
        with Session(self.engine) as session:
            data = session.execute(select(UserAuth).where(UserAuth.login==login)).first()
            
        return data


        
