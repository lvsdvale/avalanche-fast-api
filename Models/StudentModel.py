from sqlalchemy import Integer, String, Column, Boolean
from sqlalchemy.orm import relationship
from UserModel import UserModel
from AthleteModel import AthleteModel
from core.config import settings


class StudentModel(settings.DBBaseModel):
    __tablename__ = 'Student'

    id = Column(Integer, primary_key=True, autoincrement=True)
    ra = Column(Integer, unique=True)
    course = Column(String(256),  nullable=False)
    graduated = Column(Boolean, default=False)
    user = relationship(
        'UserModel',
        back_populates="student",
       )
    athlete = relationship(
        'AthleteModel',
        back_populates="student",
        uselist=False,
       )  
   