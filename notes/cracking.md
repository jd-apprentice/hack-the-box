# Cracking

## Hashes

https://hashes.com/en/tools/hash_identifier

```bash
hashid <HASH>
```

https://hashcat.net/wiki/doku.php?id=example_hashes

```bash
hashcat -m <MODE> <HASH> <WORDLIST>
hashcat -m 22931 ../wordlists/users/ssh_david.txt ../wordlists/rockyou.txt
```

## SSH

https://robertholdsworthsecurity.medium.com/how-to-crack-an-ssh-private-key-passphrase-ab7dd1583178

```bash
ssh2john id_rsa > id_rsa.hash
john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa.hash
```

## ZIP

```bash
sudo apt install fcrackzip
fcrackzip -u -D -p rockyou.txt <FILE>
```