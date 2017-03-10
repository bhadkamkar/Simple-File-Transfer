import subprocess

command1 = subprocess.Popen(["python", "server.py", "--server-ip", "127.0.0.1", "--server-port", "8080"])
command2 = subprocess.Popen(["python", "cli.py", "--server-ip", "127.0.0.1", "--server-port", "8080"])