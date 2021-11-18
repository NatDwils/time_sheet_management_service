from fastapi import APIRouter, File, UploadFile
from src.models.user import User
from src.repository.db import task
import pandas as pd
from src.resource.task import get_task,get_task_sheet,update_task

user = APIRouter()


@user.get('/getall_task_sheet/')
async def get_task_sheet():
   get_task_sheet()


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
   update_task()


@user.get('/{user_id}')
async def get_task(id, start_date: int = 0, end_date: int = 10):\
    get_task()
