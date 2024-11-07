from sqlalchemy import String,UUID,DATETIME,DATE
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
import uuid
from sqlalchemy.orm import DeclarativeBase
from sqlalchemy.orm import Session
from sqlalchemy import URL

class Base(DeclarativeBase):
  pass

def generate_uuid():
    return str(uuid.uuid4())


class User(Base):
   __tablename__="users"
   __table_args__={'schema': 'user_mgmt'}
   user_id:Mapped[UUID] = mapped_column(UUID,primary_key=True,default=generate_uuid)
   fname:Mapped[str] = mapped_column(String(20))
   lname:Mapped[str] = mapped_column(String(20))
   dob:Mapped[DATE] = mapped_column(DATETIME)
   password:Mapped[str] = mapped_column(String(255),name="pwd")

from sqlalchemy import create_engine

url_object = URL.create(
    "postgresql+psycopg2",
    username="postgres",
    password="root",  # plain (unescaped) text
    host="localhost",
    database="python_tutorial",
    port="5432"
)
engine = create_engine(url_object)
with Session(engine) as session:
   user = User(fname="Rithuik",lname="Yerr",dob='2024-01-01',password="sfwef")
   session.add(user)
   session.commit()