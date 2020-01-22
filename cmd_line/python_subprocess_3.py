import subprocess

ps1 = subprocess.run(['ls'], universal_newlines=True, stdout=subprocess.PIPE)
ps2 = subprocess.run(['cowsay'], universal_newlines=True, input=ps1.stdout)

# https://stackoverflow.com/questions/34147353/python-subprocess-chaining-commands-with-subprocess-run
# https://docs.python.org/3/library/subprocess.html