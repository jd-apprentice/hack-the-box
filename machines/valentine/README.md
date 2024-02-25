# Valentine

User FLAG
-----

1. Scan ports with nmap
2. Scan for vulnerabilities with nmap scripts
3. Discovery with dirsearch
4. Download `hype_key`
5. Use CVE-2014-0224 to obtain the hype_key password
6. SSH into the machine with the hype_key and `hype` user
7. Obtain the user flag

## Versions

Apache 2.2.22
PHP 5.3.10
SSH-2.0-OpenSSH_5.9p1 Debian-5ubuntu1.10

## CVEs

CVE-2011-1002
CVE-2014-0224 (This one)
CVE-2014-0160
CVE-2014-3566

## Passwords
heartbleed.....

Root Flag
-----

1. Enumerate files and processes
2. Access the root tmux session
3. Read the root flag

## Enumeration

```shell
id || (whoami && groups) 2>/dev/null
# uid=1000(hype) gid=1000(hype) groups=1000(hype),24(cdrom),30(dip),46(plugdev),124(sambashare)
sudo -l
# Password required
env
# Nothing useful
cat /var/log/auth.log
# Permission denied
cat /etc/crontab
# Empty
```

```shell
ps aux | grep root
# root 1028 0.0 .01 26416 1680 ? Ss 10:28 0:00 /usr/bin/tmux -S /.devs/devs_sess
```

root is running a tmux session, we can access it, first and foremost, we need to start tmux by typing `tmux` in the terminal.

then we can access the session with the following command:

```bash
tmux -S <session_name>
```

In this session, we got root privileges and we can read the root flag.

Congratulations! You have successfully completed the Valentine machine.

## Links

- https://tmuxcheatsheet.com/
- https://gist.github.com/RitamDey/128bb6dbfa6a7a1d753182341d57a9c7
- https://stackoverflow.com/questions/73795935/sign-and-send-pubkey-no-mutual-signature-supported
- https://docs.metasploit.com/docs/using-metasploit/getting-started/nightly-installers.html