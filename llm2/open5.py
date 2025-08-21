from llm2 import openAiModel, makeMsg, openAiModelArg

def test(prompt):
    OpenModel=openAiModel()
    response =OpenModel.images.generate(
        model="dall-e-3",
        prompt= prompt,
        size="1024x1024",
        quality="standard",
        n=1,
    )
    image_url = response.data[0].url
    print(image_url)

if __name__ == "__main__":
    prompt="갈색 강아지와 흰색 고양이 사진 만들어줘"
    test(prompt)