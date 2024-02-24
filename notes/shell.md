# Shell

## Interactive Shell

After obtaining a reverse shell, you can use the following commands to upgrade the shell to a TTY shell.

```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
```

```bash
script /dev/null -c bash
```

```shell
CTRL+Z
stty raw -echo; fg
```

```shell
export TERM=xterm
export SHELL=bash
```

## Reverse Shell

https://www.revshells.com/