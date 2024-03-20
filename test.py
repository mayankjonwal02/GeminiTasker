import os

venv_path = os.path.join(os.path.dirname(__file__), "myenv\\Scripts\\python.exe")  # Assuming Python executable is 'python.exe'

if os.path.exists(venv_path):
    print("Path exists:", venv_path)
else:
    print("Path does not exist:", venv_path)
