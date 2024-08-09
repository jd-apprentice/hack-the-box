User FLAG
-----

1. Scan with `nmap`
2. Found port 22 and 80
3. Scan with `dirsearch`
4. Scan with `wfuzz`

```shell
 wfuzz -c --hh=15949 -w $HOME/Documents/Security/wordlists/subdomains-top1million-110000.txt -H 'Host: FUZZ.board.htb' -u http://board.htb/ 
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://board.htb/
Total requests: 114441

=====================================================================
ID           Response   Lines    Word       Chars       Payload                                                                                                  
=====================================================================

000000072:   200        149 L    504 W      6360 Ch     "crm"
```

5. Found `crm.board.htb`
6. Dolibarr 17.0.0
7. Tried admin admin and it worked
8. https://www.swascan.com/security-advisory-dolibarr-17-0-0/


```shell
-rw-r--r-- 1 root root 813 Feb  1  2020 /usr/share/bash-completion/completions/postfix
-rw-r--r-- 1 root root 69 Jun 27  2023 /etc/php/7.4/mods-available/ftp.ini                                                                                                          
-rw-r--r-- 1 root root 69 May  1 03:11 /usr/share/php7.4-common/common/ftp.ini
lrwxrwxrwx 1 root root 24 Sep 17  2023 /etc/mysql/my.cnf -> /etc/alternatives/my.cnf
-rw-r--r-- 1 root root 81 May 13 23:40 /var/lib/dpkg/alternatives/my.cnf
-rw-r--r-- 1 www-data www-data 5265 Mar  4  2023 /var/www/html/crm.board.htb/htdocs/admin/system/database.php

The password hash is from the {SSHA} to 'structural'
drwxr-xr-x 2 root root 4096 May 13 23:40 /etc/ldap

find / -name conf.php
$dolibarr_main_url_root='http://crm.board.htb';
$dolibarr_main_document_root='/var/www/html/crm.board.htb/htdocs';
$dolibarr_main_url_root_alt='/custom';
$dolibarr_main_document_root_alt='/var/www/html/crm.board.htb/htdocs/custom';
$dolibarr_main_data_root='/var/www/html/crm.board.htb/documents';
$dolibarr_main_db_host='localhost';
$dolibarr_main_db_port='3306';
$dolibarr_main_db_name='dolibarr';
$dolibarr_main_db_prefix='llx_';
$dolibarr_main_db_user='dolibarrowner';
$dolibarr_main_db_pass='serverfun2$2023!!';
$dolibarr_main_db_type='mysqli';
$dolibarr_main_db_character_set='utf8';
$dolibarr_main_db_collation='utf8_unicode_ci';
// Authentication settings
$dolibarr_main_authentication='dolibarr';

mysql -h localhost -P 3306 -u dolibarrowner -p dolibarr

$2y$10$VevoimSke5Cd1/nX1Ql9Su6RstkTRe7UX1Or.cm8bZo56NjCMJzCm
$2y$10$gIEKOl7VZnr5KLbBDzGbL.YuJxwz5Sdl5ji3SEuiUSlULgAhhjH96

ls /usr/share/xsessions/
```
## Links

- https://www.swascan.com/security-advisory-dolibarr-17-0-0/
- https://unix.stackexchange.com/questions/366052/how-to-determine-which-desktop-environment-is-installed-from-the-shell
- https://github.com/MaherAzzouzi/CVE-2022-37706-LPE-exploit

## Versions

- Sudo version 1.8.31
- Dolibarr 17.0.0