## Privilege Escalation 🪜

First steps on what to do after getting a shell on a machine. After stabilizing the shell.

```shell
sudo -l # Check for sudo privileges
env # Check for environment variables
find / -perm -4000 -type f 2>/dev/null # Check for files with `setuid` bit set
cat /var/log/auth.log
cat /etc/crontab
```

## Enumeration

```bash
ps aux #List running processes
id || (whoami && groups) 2>/dev/null #Info about me
cat /etc/passwd | cut -d: -f1 #List all users
cat /etc/passwd | grep "sh$" #List users with console
awk -F: '($3 == "0") {print}' /etc/passwd #List superusers
w #Currently logged users
last | tail #Login history
lastlog #Last log of each user
#List all users and their groups
for i in $(cut -d":" -f1 /etc/passwd 2>/dev/null);do id $i;done 2>/dev/null | sort
gpg --list-keys 2>/dev/null #Current user PGP keys
```

```bash
date 2>/dev/null #Date
(df -h || lsblk) #System stats
lscpu #CPU info
lpstat -a 2>/dev/null #Printers info
```

If stuck, check the [Privilege Escalation](https://book.hacktricks.xyz/linux-hardening/privilege-escalation) section of HackTricks.