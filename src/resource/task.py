
from src.models.user import User
from src.repository.db import task
from bson.objectid import ObjectId
from src.schemas.user import userEntity, usersEntity

def get_task_sheet():
    print(task.find())
    print(usersEntity(task.find()))
    return usersEntity(task.find())

def update_task(id, task_update_request: User):
    task.update_one({"_id": ObjectId(id)},
                    {"$set": {"name": task_update_request.name, "task": task_update_request.task,
                              "start_date": task_update_request.start_date, "end_date": task_update_request.end_date}})
    return userEntity(task.find_one({"_id": ObjectId(id)}))

def get_task(id, start_date: int = 0, end_date: int = 10):
    return userEntity(task.find_one({"_id": ObjectId(id)}))
