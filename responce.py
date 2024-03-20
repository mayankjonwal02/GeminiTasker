import subprocess

# Add the remote origin
subprocess.run(["git", "remote", "add", "origin", "https://github.com/mayankjonwal02/GeminiTasker.git"])

# Commit any changes
subprocess.run(["git", "commit", "-am", "Add files"])

# Push all files
subprocess.run(["git", "push", "-u", "origin", "main"])