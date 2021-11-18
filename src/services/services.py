from fastapi import APIRouter, File, UploadFile

from src.models.user import User
from src.repository.db import task
import pandas as pd
from bson.objectid import ObjectId
from src.schemas.user import userEntity, usersEntity

user = APIRouter()


@user.get('/getall_task_sheet/')
async def get_task_sheet():
    print(task.find())
    print(usersEntity(task.find()))
    return usersEntity(task.find())


@user.post("/upload_task_sheet/")
async def create_task_sheet(excel_file: UploadFile = File(...)):
    print(excel_file.filename)
    contents = excel_file.file.read()
    df = pd.read_excel(contents)
    print(df[['Unnamed: 0', 'Unnamed: 1']])
    document = df.to_dict(orient="records")
    print(document)
    task.insert_many(document)


@user.put('/{id}')
async def update_task(id, task_update_request: User):
    task.update_one({"_id": ObjectId(id)},
                    {"$set": {"name": task_update_request.name, "task": task_update_request.task,
                              "start_date": task_update_request.start_date, "end_date": task_update_request.end_date}})
    return userEntity(task.find_one({"_id": ObjectId(id)}))


@user.get('/{id}')
async def get_task(id):
    return userEntity(task.find_one({"_id": ObjectId(id)}))


@user.get('/{user_id}')
async def get_task(id, start_date: int = 0, end_date: int = 10):
    return userEntity(task.find_one({"_id": ObjectId(id)}))
