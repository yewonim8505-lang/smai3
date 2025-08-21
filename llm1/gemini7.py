from io import BytesIO

import requests
from PIL.Image import Image

from llm1.gemini4 import prompt
from myllm.myapi import geminimodel

def test(prompt,img):
    model = geminimodel()
    response = model.generate_content([prompt,img])
    print(response.text)

if __name__ == '__main__':
    image_url = "https://oaidalleapiprodscus.blob.core.windows.net/private/org-9qyO8DBfZVE7lQkjKIV1E3u9/user-6iEJ0m5gbHH0s0nAsMuCmNs6/img-QASE3O3BPZGtzBbWetlCmOXq.png?st=2025-07-29T06%3A07%3A18Z&se=2025-07-29T08%3A07%3A18Z&sp=r&sv=2024-08-04&sr=b&rscd=inline&rsct=image/png&skoid=d505667d-d6c1-4a0a-bac7-5c84a87759f8&sktid=a48cca56-e6da-484e-a814-9c849652bcb3&skt=2025-07-29T05%3A58%3A18Z&ske=2025-07-30T05%3A58%3A18Z&sks=b&skv=2024-08-04&sig=CkI1F6/7uS0aVBLRdFB%2BstcZ4fSHRf1zuxFGBSWIi6I%3D"
    response_image = requests.get(image_url)
    img = Image.open(BytesIO(response_image.content))
    prompt="이미지에 있는 음료의 영양성분과 칼로리 당함유 양을 알려줘"
    test(prompt,img)
