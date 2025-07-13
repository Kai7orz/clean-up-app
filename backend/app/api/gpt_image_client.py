import base64
from openai import OpenAI 
from app.utils.make_mask import make_mask
from app.utils.image_to_base64 import image_to_base64

# 引数:image のpath 
# 出力:GPT API からのレスポンスイラストオブジェクト
def call_gpt_with_image(image_path):
    client = OpenAI()
    # base64_image = image_to_base64(image_path)
    prompt = "画像をイラスト化して"
    model = "dall-e-2"
    mask_output_path = make_mask(image_path)

    with open(image_path,"rb") as image_file,open(mask_output_path,"rb") as mask_file:
        result = client.images.edit(
            model=model,
            image=image_file,
            mask=mask_file,
            prompt=prompt
        )

        response_image_base64 = result.data[0].b64_json 
        image_bytes = base64.base64decode(response_image_base64)

        with open("illust_image.png","wb") as f:
            f.write(image_bytes)

# openAI からのレスポンスはローカルに保存されないので，web 上でファイルをオープンしてローカルに書き込む処理を入れておく

