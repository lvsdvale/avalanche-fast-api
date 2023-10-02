from sqlalchemy import Integer, String, Column, Boolean, ForeignKey
from sqlalchemy.orm import relationship, Mapped, mapped_column, DeclarativeBase
from StudentModel import StudentModel


from core.config import settings


class UserModel(settings.DBBaseModel):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True, autoincrement=True)
    CPF = Column(String(256), unique=True,  nullable=False)
    name = Column(String(256),  nullable=False)
    phoneNumber = Column(Integer(11), unique=True)
    email = Column(String(256), index=True, nullable=False, unique=True)
    password = Column(String(256), nullable=False)
    admin = Column(Boolean, default=False)
    student = relationship(
        'StudentModel',
        back_populates="user",
        uselist=False,
       ) 
   


