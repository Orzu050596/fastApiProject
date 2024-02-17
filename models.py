from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Boolean
from database import Base

class Question(Base):
    __tablename__ = "questions"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    question_text = Column(String, index=True)

class Choice(Base):
    __tablename__ = "choices"
    id = Column(Integer, primary_key=True, autoincrement=True, index=True)
    choice_text = Column(String, index=True)
    is_correct = Column(Boolean, default=False)
    question_id = Column(Integer, ForeignKey('questions.id'))