# Fuzzing

## Wfuzz

https://github.com/xmendez/wfuzz

```bash
wfuzz --hw=153 -c -t 200 -w ~/Documents/Security/wordlists/common.txt http://40.121.87.195:60004/\?file\=..//FUZZ.txt
```

- `--hw` : Hide words with length equal to or less than the specified value
- `-c` : Show output in color
- `-t` : Number of threads
- `-w` : Wordlist to use
- `FUZZ` : Where the payload will be placed