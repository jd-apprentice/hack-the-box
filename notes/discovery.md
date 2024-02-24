# Discovery

## Feroxbuster

https://github.com/epi052/feroxbuster

```bash
`feroxbuster --insecure -u http://10.10.10.75/nibbleblog -o ferox -w ~/Documents/Security/wordlists/php.txt`
```

- `--insecure` : Ignore SSL certificate errors
- `-u` : URL to scan
- `-o` : Output directory
- `-w` : Wordlist to use

## Dirsearch

https://github.com/maurosoria/dirsearch

```bash
dirsearch -u 40.121.87.195:60000 -w ~/Documents/Security/wordlists/raft-medium-directories.txt -t 100
```

- `-u` : URL to scan
- `-w` : Wordlist to use
- `-t` : Number of threads