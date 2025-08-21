from llm2 import openAiModel, makeMsg, openAiModelArg


def test(prompt):
    modelname="gpt-4o"
    msg=makeMsg("너는 무서운 한국어 선생님",prompt)
    result=openAiModelArg(modelname,msg)
    print(result)


if __name__ == "__main__":
    prompt="우간다의 수도가 어디야"
    test(prompt)