from hashlib import sha256
from sqlalchemy import create_engine
from sqlalchemy.orm import Session,sessionmaker
from sqlalchemy import URL
from sqlalchemy import select


class DBService():

    def __init__(self):
        self.url = URL.create("postgresql+psycopg2",username="postgres",password="P4$$w0rd",host="database-1.cvqgcygm0awc.ap-south-1.rds.amazonaws.com",database="postgresdb1",port="5432")
        self.engine = engine = create_engine(self.url)
    
    def persist_obj(self,obj):
        with Session(self.engine,expire_on_commit=False) as session:
            session.add(obj)
            session.commit()
        return obj

    def persist_obj_list(self,lis:list):
        with Session(self.engine) as session:
            session.add_all(lis)
            session.commit()


        
