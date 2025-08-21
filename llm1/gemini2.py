import google.generativeai as genai


from dotenv import load_dotenv
import os

import PIL.Image

from llm1.gemini1 import response

load_dotenv()

GOOGLE_API_KEY=os.getenv("GOOGLE_API_KEY")
genai.configure(api_key=GOOGLE_API_KEY)

model = genai.GenerativeModel("gemini-2.0-flash")

from PIL import Image
import os

# 이미지 경로: 바탕화면에 있는 a.jpg
# 사용자 이름은 본인의 Windows 사용자 이름으로 바꿔야 합니다
img_path = r"C:\Users\user\Desktop\a.jpg"

# 이미지 열기
img = Image.open(img_path)
img.show()

print(response.text)