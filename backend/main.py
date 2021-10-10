# required libraries
from fastapi import FastAPI
from config.config import setting
#======================================

app = FastAPI(title=setting.PROJECT_TITLE, version= setting.PROJECT_VERSION)

@app.get("/")
def greeter():
    return {"Hello": "Universe!!"}

# uvicorn main:app --reload
