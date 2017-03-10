import subprocess
import os
from time import sleep


command1 = subprocess.Popen(["python", "server.py", "--server-ip", "127.0.0.1", "--server-port", "8083"])
command2 = subprocess.Popen(["python", "cli.py", "--server-ip", "127.0.0.1", "--server-port", "8083"])

sleep(5)
command1.terminate()
