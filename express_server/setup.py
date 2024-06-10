import subprocess

# Load commands from the commands file.
with open("commands.txt", "r") as fh:
# readlines() to get lines
    cmds = fh.readlines()
    for item in cmds:
# Run each command in Python.
        subprocess.run(item.split(" "))
