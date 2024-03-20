from GeminiTest import GetGeminiResponce

while True:
    prompt = input("Enter Prompt : ")
    if(prompt.lower == "stop"):
        break
    else:
        GetGeminiResponce(prompt)