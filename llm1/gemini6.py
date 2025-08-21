from llm2 import geminimodel


def test(prompt):
    model = geminimodel()
    response = model.generate_content(prompt)
    print(response.text)


if __name__ == '__main__':
    code_prompt = "Python으로 피보나치 수열을 계산하는 함수를 작성해 줘."
    test(code_prompt)
