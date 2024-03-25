# Cracking

## Hashes

[hash identifier](https://hashes.com/en/tools/hash_identifier)

```bash
hashid <HASH>
```

[example hashes](https://hashcat.net/wiki/doku.php?id=example_hashes)

```bash
hashcat -m <MODE> <HASH> <WORDLIST>
hashcat -m 22931 ../wordlists/users/ssh_david.txt ../wordlists/rockyou.txt
```

### Mash attack

When we know the password length or the password pattern

```bash
hashcat -a 3 -m 1400 <HASH> <PASSWORD><MASK> # https://hashcat.net/wiki/doku.php?id=mask_attack
```

## SSH

[read](https://robertholdsworthsecurity.medium.com/how-to-crack-an-ssh-private-key-passphrase-ab7dd1583178)

```bash
ssh2john id_rsa > id_rsa.hash
zip2john <ZIP> > <ZIP>.text
john --wordlist=/usr/share/wordlists/rockyou.txt id_rsa.hash
john --wordlist=/usr/share/wordlists/rockyou.txt <ZIP>.text
```

## ZIP

```bash
sudo apt install fcrackzip
fcrackzip -u -D -p rockyou.txt <FILE>
```

## Find strings

We can use `strings` to find strings in a file

It can be a database, a binary, a .exe, a disk, etc.

```bash
strings <FILE>
```