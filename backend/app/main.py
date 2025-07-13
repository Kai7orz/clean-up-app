from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel 
from typing import Union 
import sys 
from utils.resize_image import resize_image
from utils.make_mask import make_mask

class Item(BaseModel):
    name: str 
    description: Union[str,None] = None 
    price: float 
    tax: Union[float,None] = None

def MyDebugs():
    image_path = "assets/images/test_image.jpg"
    resized_input_path = resize_image(image_path)
    custom_output_path = "assets/images/mask.jpg"
    mask_output = make_mask(image_path=resized_input_path,output_path=custom_output_path)


MyDebugs()



app = FastAPI() 

origins = [
    "http://localhost:80",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware, 
    allow_origins=origins,
    allow_credentials=True, 
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/") 
def read_root():
    images = [{"message":"Hello World!"},{"message":"hello image"}]
    return images

@app.get("/users/{user_id}")
async def read_user(user_id: int):
    return {"user_id": user_id}



# @app.post("/users/{user_id}/images/{image_url}")
# async def upload_image(user_id:int , image_url:str):
