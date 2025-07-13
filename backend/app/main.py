from fastapi import FastAPI 
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel 
from typing import Union 
import sys 
from utils.resize_image import resize_image
from utils.make_mask import make_mask
from utils.convert_rgb_to_rgba import convert_to_rgba_image
from api.gpt_image_client import call_gpt_with_image

class Item(BaseModel):
    name: str 
    description: Union[str,None] = None 
    price: float 
    tax: Union[float,None] = None

# def MyDebugs():
#     image_path = "assets/images/test_image.jpg"
#     resized_image_path = resize_image(image_path)
#     converted_image_path = convert_to_rgba_image(resized_image_path,mask=False)
   
#     custom_output_path = "assets/images/mask.png" 
#     #RGB 形式のMask 画像のパス
#     mask_raw_output_path = make_mask(image_path=resized_image_path,output_path=custom_output_path)
#     #RGBA 形式変換後の画像のパス
#     converted_mask_path=convert_to_rgba_image(mask_raw_output_path,mask=True)

#     call_gpt_with_image(converted_image_path,converted_mask_path)
    

# MyDebugs()



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

@app.post("/users/{user_id}/")
async def get_illustration(image_id: int=0):
    # 画像をファイルオブジェクトとして読み込む
    # client へバイナリpng として送信する処理

    return 



# @app.post("/users/{user_id}/images/{image_url}")
# async def upload_image(user_id:int , image_url:str):
