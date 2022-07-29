import readline
from subprocess import Popen, PIPE
import sys
import random
import pwn
import time
import fileinput
import requests


conn = pwn.remote('localhost',9001)
conn.recvuntil(b'JSON input:')
while True:
   
    conn.sendline(b'{"apiKey":"1337d74c985b01ab9d4f996690a8dde658ec307313c1a521810bdcff6d964b4e", "x":"qqqqqqqqqqqqqqqq","apiKey":"","operation":"getSshKey" }')
    conn.recvuntil(b'Your ciphertext: ')
    ciphertext = bytearray(conn.recvline().strip())
    b = 180
    if ciphertext[b] == 50:
      ciphertext[b] = 49
    else:
      ciphertext[b] = 50
    ciphertext.strip()
    conn.recvline()
    conn.recvline()
    conn.sendline(ciphertext)
    st = conn.recvuntil(b'JSON input:')
    if b'JSON parse error: SyntaxError: Unexpected' not in st:
        print(st)
        break
    # print(st) 

conn.close()

# conn.sendline('{"apiKey":"1337d74c985b01ab9d4f996690a8dde658ec307313c1a521810bdcff6d964b4e", "x":"qqqqqqqqqqqqqqqq","apiKey":"","operation":"getFlag" }')