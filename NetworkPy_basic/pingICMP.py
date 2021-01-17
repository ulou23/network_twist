import subprocess
import  shlex

com_line="ping -c 1 www.dwutygodnik.com"
args=shlex.split(com_line)
try:
    subprocess.check_call(args,stdout=subprocess.PIPE,stderr=subprocess.PIPE)
    print("server up")
except subprocess.CalledProcessError:
    print("failed ping")

    