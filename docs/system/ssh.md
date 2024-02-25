# SSH

SSH (Secure Shell) is a network protocol that allows secure communication between two computers. It is used to log into a remote machine and execute commands.

## Connect via ssh

```bash
ssh user@<IP>
```

## Convert putty to openssh

```bash
sudo apt install putty-tools
puttygen putty.ppk -O private-openssh -o id_rsa
chmod 600 id_rsa
```

## Bruteforce

- [ssb](https://github.com/pwnesia/ssb)
- [hydra](https://github.com/vanhauser-thc/thc-hydra)

## Known Username

```bash
ssb -p <PORT> -w <WORDLIST> <USER>@<IP>
hydra -l <USER> -t <THREADS> -P <WORDLIST> ssh://<IP>
```

## Private Key

```bash
ssh -i id_rsa <USER>@<IP>
```

## IdentitiesOnly

```bash
ssh -o IdentitiesOnly=yes -i id_rsa <USER>@<IP>
```

## Crack Private Key

[ssh2john](https://github.com/openwall/john/blob/bleeding-jumbo/run/ssh2john.py)

```bash
ssh2john id_rsa > id_rsa.hash
john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa.hash
```