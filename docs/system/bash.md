# Bash

## Encode and decode base64

```bash
echo "id" | base64
# aWQK
echo "aWQK" | base64 -d | bash
uid=1000(user)
```

## Check if a file exists

```bash
if [ -f /etc/passwd ]; then
    echo "File exists"
else
    echo "File does not exist"
fi
```

## Find files

```bash
find / -name "passwd"
```

## Find files by extension

```bash
find / -name "*.txt"
```