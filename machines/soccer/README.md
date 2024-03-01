User FLAG
-----

1. Scan target
2. Enter port 80
3. Add dns entry to /etc/hosts
4. Enumerate directories
5. Find tinyfilemanager
6. Find credentials
7. Login to tinyfilemanager
8. Upload reverse shell
9. Enumerate machine
10. Found another host from the nginx configuration
11. Explore application
12. Create an account
13. Login with that account
14. Check ticket part
15. Try server-side-template-injection (nope)
16. Try sql injection with websocket url (sqlmap)
17. Obtain DB names
18. Obtain user to SSH
19. Get user flag

## Info

Nothing at local/session storage -- not relevant
Nothing in the source code -- not relevant in first app

There is a path /tiny which uses tinyfilemanager -- yes

Credentials
Default username/password: admin/admin@123 -- yes

Expressjs running on new hostname -- yes
Set-Cookie: connect.sid=s%3AW6OeVgCFtvL35TpGKSPBD4iY3_0S7OU2.ITMDSN4vKobEvEKQAB4Juf9QHkydF1a6A5Wea8TVlwI; -- not relevant

Found this code in the source -- yes

```js
var ws = new WebSocket("ws://soc-player.soccer.htb:9091"); // We can use this later!
window.onload = function () {

var input = document.getElementById('id');

function sendText() {
    var msg = input.value;
    if (msg.length > 0) {
        ws.send(JSON.stringify({
            "id": msg
        }))
    }
    else append("????????")
}
}

ws.onmessage = function (e) {
    append(e.data)
}

function append(msg) {
    let p = document.querySelector("p");
    p.textContent = msg
}
```

As we can see the payload sends an id which is the message.
After this we can scan it with sqlmap sending an id

```bash
sqlmap -u "ws://soc-player.soccer.htb:9091" --data '{"id": "*"}' --dbs --threads 10 --
level 5 --risk 3 --batch
```

Created `sqlmap.log`

At this point we have the db name, we can dump it with sqlmap too, and there we have ssh user to obtain user flag.

### Inside machine

Ports -- not relevant
33060
3306
80
53
22
3000
9091

Versions -- not relevant
mysql  Ver 8.0.31-0ubuntu0.20.04.2 for Linux on x86_64 ((Ubuntu))
Sudo version 1.8.31
Linux soccer 5.4.0-135-generic

SGID -- not relevant
daemon daemon 55K Nov 12  2018 /usr/bin/at  --->  RTru64_UNIX_4.0g(CVE-2002-1614)

Routes -- not relevant
/usr/lib/mysql/plugin/component_mysqlbackup.so
/etc/mysql/debian.cnf
/data                                                                                     
/vagrant
/snap/core20/1695/etc/cloud/cloud.cfg

-- yes
```bash
ls -al /etc/nginx/sites-enabled
total 8
drwxr-xr-x 2 root root 4096 Dec  1  2022 .
drwxr-xr-x 8 root root 4096 Nov 17  2022 ..
lrwxrwxrwx 1 root root   34 Nov 17  2022 default -> /etc/nginx/sites-available/default
lrwxrwxrwx 1 root root   41 Nov 17  2022 soc-player.htb -> /etc/nginx/sites-available/soc-player.htb
```

-- not relevant
From '/etc/mysql/mysql.conf.d/mysqld.cnf' Mysql user: user              = mysql                                                                                                     
Found readable /etc/mysql/my.cnf                                                                                                                                                    
!includedir /etc/mysql/conf.d/                                                                                                                                                      
!includedir /etc/mysql/mysql.conf.d/q

## Versions

OpenSSH 8.2p1 Ubuntu 4ubuntu0.5
nginx 1.18.0
Tiny File Manager 2.4.3
back-end DBMS: MySQL >= 5.0.12

## Services

xmltec-xmlmail

## Links

- https://tinyfilemanager.github.io/
- https://github.com/sqlmapproject/sqlmap