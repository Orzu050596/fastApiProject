from fastapi import FastAPI, status, Depends
from pydantic import BaseModel
from typing import List, Annotated

from starlette import status

import models

from database import engine, SessionLocal

app = FastAPI()
models.Base.metadata.create_all(bind=engine)


class ChoiceBase(BaseModel):
    choice_text: str
    is_correct: bool


class QuestionBase(BaseModel):
    question_text: str
    choices: List[ChoiceBase]


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


db_dependency = Annotated[SessionLocal, Depends(get_db)]


@app.post("/questions/")
async def create_question(questions: QuestionBase, db: db_dependency):
    db_question = models.Question(**questions.dict())
    db.add(db_question)
    db.commit()
    db.refresh(db_question)
    return db_question
