from db_gino import TimeBaseModel
from sqlalchemy import BigInteger,Column,Integer,String, sql

class User(TimeBaseModel):
    __tablename__ = 'users'
    id = Column(BigInteger,primary_key=True)
    name = Column(String(100))
    email = Column(String(100))
    referal = Column(BigInteger)
    
    query: sql.Select