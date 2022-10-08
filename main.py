from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.params import Body

app = FastAPI()



@app.get("/")
async def home():
    return{"message":"Homepage"}


@app.post("/createpost/")
async def create_post(payload:dict=Body(...)):
    print(payload)
    return {"message":f"The title of post is {payload['title']} and content is {payload['content']}"}