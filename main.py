from fastapi import FastAPI
from dotenv import dotenv_values
from pymongo import MongoClient
from routes import router as cv_router

config = dotenv_values(".env")

app = FastAPI()

@app.on_event("startup")
def startup_db_client():
    app.mongodb_client = MongoClient(config["MONGODB_URI"])
    app.database = app.mongodb_client[config["MONGODB_NAME"]]

@app.on_event("shutdown")
def shutdown_db_client():
    app.mongodb_client.close()

app.include_router(cv_router, tags=["items"], prefix=config["API_V1_STR"])