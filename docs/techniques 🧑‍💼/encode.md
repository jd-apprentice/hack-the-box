# Encode

Encoding is the process of converting data from one form to another. It is used to protect data from unauthorized access and to ensure that the data is not corrupted during transmission.

[base64](https://www.base64encode.org/)

## Encode a value with bash

[read](https://askubuntu.com/a/178546)

```bash
echo -n "id" | base64
## Result: aWQ=
```

## Execute a command encoded

```bash
echo "aWQ=" | base64 --decode | sh
## Result: uid=0(root) gid=0(root) groups=0(root)
```