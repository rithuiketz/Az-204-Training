from sqlalchemy import String,UUID,DATETIME,DATE
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
import uuid
from sqlalchemy.orm import DeclarativeBase
import hashlib
from datetime import datetime

class Base(DeclarativeBase):
  pass

def generate_uuid():
    return str(uuid.uuid4())

def generate_random_password():
  password = str(datetime.now())
# Create a SHA-256 hash object
  hash_object = hashlib.sha256()
# Convert the password to bytes and hash it
  hash_object.update(password.encode())
# Get the hex digest of the hash
  hash_password = hash_object.hexdigest()
  return hash_password
    

class User(Base):
   __tablename__="users"
   __table_args__={'schema': 'user_mgmt'}
   user_id:Mapped[UUID] = mapped_column(UUID,primary_key=True,default=generate_uuid)
   fname:Mapped[str] = mapped_column(String(20))
   lname:Mapped[str] = mapped_column(String(20))
   dob:Mapped[DATE] = mapped_column(DATETIME)
   password:Mapped[str] = mapped_column(String(255),name="pwd",default=generate_random_password)