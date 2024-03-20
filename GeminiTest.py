import google.generativeai as genai
import os
import subprocess
import re

def save_to_parent_dir(code , filename):
    script_dir = os.path.dirname(os.path.abspath(__file__))
    filepath = os.path.join(script_dir , filename+".py")

    with open(filepath,"w") as f:
        f.write(code)
    venv_path = os.path.join(os.path.dirname(__file__), "myenv", "Scripts", "python")
    subprocess.run([venv_path , filepath])
    

def GetGeminiResponce(prompt):
    genai.configure(api_key="AIzaSyBDY_QldI4t266RqmTNwWTBCMgcy91YQyQ")
    model = genai.GenerativeModel("gemini-pro")
    

    responce = model.generate_content("Get Python code for " + prompt + " and use python and it's libraries")
    essential_code = re.findall(r"`python\n(.*?)\n`", responce.text, flags=re.DOTALL)[0]
    # responce.text[9:-3]
    print(essential_code)

    save_to_parent_dir(essential_code,"responce")

    print("code saved .....")

