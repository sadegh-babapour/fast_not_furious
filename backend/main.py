# required libraries
from fastapi import FastAPI
from sqlalchemy.engine import create_engine
from database.base_class import Base
from config.config import setting
from database.session import engine

#======================================

def create_tables():
    Base.metadata.create_all(bind=engine)

#======================================





# uvicorn main:app --reload
def run_forrest_run():
    app = FastAPI(title=setting.PROJECT_TITLE, version= setting.PROJECT_VERSION)
    create_tables()
    return app

app = run_forrest_run()








@app.get("/")
def greeter():
    return {"Hello": "Universe!!"}