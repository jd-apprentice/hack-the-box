# Shell

## Reverse Shell

[revshell](https://www.revshells.com/) is a website that provides reverse shell payloads for various programming languages.

## Stability

When you have a reverse shell, it is important to stabilize it. This is because the shell may be unstable and may not be able to run certain commands. You can stabilize the shell by running the following command.

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
stty rows 48 columns 170
```