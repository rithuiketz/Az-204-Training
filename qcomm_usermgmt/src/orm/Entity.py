from sqlalchemy import String,UUID,DATETIME,DATE
from sqlalchemy.orm import Mapped
from sqlalchemy.orm import mapped_column
import uuid
from sqlalchemy.orm import DeclarativeBase
import hashlib
from datetime import datetime
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import DateTime



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
   
   communications: Mapped["UserCommunications"] = relationship("UserCommunications", back_populates="user")
   preferences : Mapped["UserPref"] = relationship("UserPref", back_populates="user")
   authMode : Mapped["UserAuth"] = relationship("UserAuth", back_populates="user")
   session : Mapped["UserSession"] = relationship("UserSession", back_populates="user")

class UserCommunications(Base):
   __tablename__="user_communications"
   __table_args__={'schema': 'user_mgmt'}
   user_id:Mapped[UUID] = mapped_column(UUID, ForeignKey('user_mgmt.users.user_id'), nullable=False)
   communication_type:Mapped[str] = mapped_column(String(10))
   value:Mapped[str] = mapped_column(String(20))
   chosen_to_communicate:Mapped[bool] = mapped_column(bool)

   user: Mapped["User"] = relationship("User", back_populates="communications")
   
class UserPref(Base):
   __tablename__="user_pref"
   __table_args__={'schema': 'user_mgmt'}
   user_id:Mapped[UUID] = mapped_column(UUID, ForeignKey('user_mgmt.users.user_id'), nullable=False)
   pref_type:Mapped[str] = mapped_column(String(10))
   value:Mapped[str] = mapped_column(String(20))

   user: Mapped["User"] = relationship("User", back_populates="preferences")
   
class UserAuth(Base):
   __tablename__="user_auth"
   __table_args__={'schema': 'user_auth'}
   user_id:Mapped[UUID] = mapped_column(UUID, ForeignKey('user_mgmt.users.user_id'), nullable=False)
   auth_mode:Mapped[str] = mapped_column(String(30))
   two_factor_enabled:Mapped[bool] = mapped_column(bool)
   pwd:Mapped[str] = mapped_column(String(255),ForeignKey('user_mgmt.users.password'), nullable=False)

   user: Mapped["User"] = relationship("User", back_populates="authMode")
   
class UserSession(Base):
   __tablename__="user_session"
   __table_args__={'schema': 'user_session'}
   user_id:Mapped[UUID] = mapped_column(UUID, ForeignKey('user_mgmt.users.user_id'), nullable=False)
   session_id:Mapped[UUID] = mapped_column(UUID, default=generate_uuid)
   start_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)
   end_time: Mapped[datetime] = mapped_column(DateTime, nullable=False)

   user: Mapped["User"] = relationship("User", back_populates="session")
   



   


