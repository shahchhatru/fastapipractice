from fastapi import FastAPI
from pydantic import BaseModel
from fastapi.params import Body
from typing import Optional

app = FastAPI()


class Item(BaseModel):
    name:str
    description:str|None=None
    rating:Optional[int]=None

@app.get("/")
async def home():
    return{"message":"Homepage"}


@app.post("/createpost/")
async def create_post(payload:dict=Body(...)):
    print(payload)
    return {"message":f"The title of post is {payload['title']} and content is {payload['content']}"}


@app.post("/createposts/")
async def create_posts(item:Item):
    print(item.dict)
    print(item)
    return {"data":item}