from fastapi import FastAPI, File, UploadFile
from services.services import user


app = FastAPI()
app.include_router(user)
#
# @app.post("/upload_task_sheet/")
# async def create_task_sheet(excel_file: UploadFile = File(...)):
# df = pd.read_excel("sample3.xlsx")
# print(df)
# document = df.to_dict(orient ="records")
# print(document)
#
# task.insert_many(document)
