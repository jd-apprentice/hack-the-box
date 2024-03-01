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
13. Login
14. Check ticket part
15. Try server-side-template-injection
16. Try sql injection (sqlmap)
17. Obtain DB names
18. Obtain user to SSH
19. Get user flag

## Info

Nothing at local/session storage
Nothing in the source code

There is a path /tiny which uses tinyfilemanager

Credentials
Default username/password: admin/admin@123

Expressjs running on new hostname
Set-Cookie: connect.sid=s%3AW6OeVgCFtvL35TpGKSPBD4iY3_0S7OU2.ITMDSN4vKobEvEKQAB4Juf9QHkydF1a6A5Wea8TVlwI;

Found this code in the source

```js
var ws = new WebSocket("ws://soc-player.soccer.htb:9091");
window.onload = function () {

var btn = document.getElementById('btn');
var input = document.getElementById('id');

ws.onopen = function (e) {
    console.log('connected to the server')
}
input.addEventListener('keypress', (e) => {
    keyOne(e)
});

function keyOne(e) {
    e.stopPropagation();
    if (e.keyCode === 13) {
        e.preventDefault();
        sendText();
    }
}

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
// let randomColor = '#' + Math.floor(Math.random() * 16777215).toString(16);
// p.style.color = randomColor;
p.textContent = msg
}
```

Created `sqlmap.log`

### Inside machine

Ports
33060
3306
80
53
22
3000
9091

Versions
mysql  Ver 8.0.31-0ubuntu0.20.04.2 for Linux on x86_64 ((Ubuntu))
Sudo version 1.8.31
Linux soccer 5.4.0-135-generic

SGID
daemon daemon 55K Nov 12  2018 /usr/bin/at  --->  RTru64_UNIX_4.0g(CVE-2002-1614)

Routes
/usr/lib/mysql/plugin/component_mysqlbackup.so
/etc/mysql/debian.cnf
/data                                                                                     
/vagrant
/snap/core20/1695/etc/cloud/cloud.cfg

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