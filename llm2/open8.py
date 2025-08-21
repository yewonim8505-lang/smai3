import urllib

from llm2 import openAiModel, makeMsg, openAiModelArg

def test(prompt):
    OpenModel=openAiModel()
    response =OpenModel.images.edit(
        model="dall-e-2",
        prompt= prompt,
        size="1024x1024",
        n=1,
        image=open("img/sample.png","rb"),
        mask=open("img/sample-mask.png","rb")
    )
    image_url = response.data[0].url
    print(image_url)
    urllib.request.urlretriev(image_url,"img/sample2.png")

if __name__ == "__main__":
    prompt="크리스마스 트리를 넣어줘"
    test(prompt)