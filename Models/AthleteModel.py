from sqlalchemy import Integer, String, Column, Boolean, DateTime
from sqlalchemy.orm import relationship
from StudentModel import StudentModel
from core.config import settings
import datetime

class AthleteModel(settings.DBBaseModel):
    __tablename__ = 'Athlete'

    id = Column(Integer, primary_key=True, autoincrement=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    student = relationship(
        'StudentModel',
        back_populates="athlete",
       )
   