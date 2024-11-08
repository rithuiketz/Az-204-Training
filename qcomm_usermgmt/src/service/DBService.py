from hashlib import sha256
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from sqlalchemy import URL


class DBService():

    def __init__(self):
        self.url = URL.create("postgresql+psycopg2",username="postgres",password="root",host="localhost",database="postgres",port="5432")

    
    def persist_obj(self,obj):
        engine = create_engine(self.url)
        with Session(engine) as session:
            session.add(obj)
            session.commit()
