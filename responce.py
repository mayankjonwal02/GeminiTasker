import subprocess
import os

# Create a git repo
subprocess.run(["git", "init"], cwd=os.getcwd())

# Add all files to the staging area
subprocess.run(["git", "add", "."], cwd=os.getcwd())

# Commit all files to the main branch
subprocess.run(["git", "commit", "-m", "Initial commit"], cwd=os.getcwd())