# You can send shell commands directly to the ssh process like so:

import subprocess
import sys

HOST = "127.0.0.1"
ssh = subprocess.Popen(["ssh",
                        "%s" % HOST],
                       stdin=subprocess.PIPE,
                       stdout=subprocess.PIPE,
                       stderr=subprocess.PIPE,
                       universal_newlines=True,
                       bufsize=0)
# send ssh commands to stdin
ssh.stdin.write("ls .\n")
ssh.stdin.write("uname -a\n")
ssh.stdin.write("uptime\n")
ssh.stdin.close()
# fetch output
for line in ssh.stdout:
    print(line)

# https://pythonspot.com/python-subprocess/
# https://bip.weizmann.ac.il/course/python/PyMOTW/PyMOTW/docs/subprocess/index.html
# https://pymotw.com/2/subprocess/
# https://www.pythonforbeginners.com/os/subprocess-for-system-administrators
# https://tryexceptpass.org/article/continuous-builds-subprocess-execution/
# https://docs.python.org/3/library/subprocess.html
# http://masnun.com/2015/09/29/python-django-running-multiple-commands-in-subprocesses.html
