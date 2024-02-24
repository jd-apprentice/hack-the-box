# Common

## Privilege Escalation

```shell
sudo -l # Check for sudo privileges
env # Check for environment variables
find / -perm -4000 -type f 2>/dev/null # Check for files with `setuid` bit set
cat /var/log/auth.log
cat /etc/crontab
```

## Wordlists

- [SecLists](https://github.com/danielmiessler/SecLists)