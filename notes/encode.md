# Encode

https://www.base64encode.org/

## Encode a value with bash

https://askubuntu.com/a/178546

```bash
echo -n "id" | base64
## Result: aWQ=
```

## Execute a command encoded

```bash
echo "aWQ=" | base64 --decode | sh
## Result: uid=0(root) gid=0(root) groups=0(root)
```