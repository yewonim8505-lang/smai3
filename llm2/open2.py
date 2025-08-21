from llm2 import openAiModel, makeMsg, openAiModelArg


def test(prompt):
    modelname="gpt-4o"
    msg=makeMsg("한문장으로 요약해줘",prompt)
    result=openAiModelArg(modelname,msg)
    print(result)

if __name__ == "__main__":
    prompt="SK하이닉스에 대해서 알려줘"
    test(prompt)