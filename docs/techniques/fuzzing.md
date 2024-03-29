# Fuzzing

Fuzzing is a technique used to find vulnerabilities in software by providing unexpected input to the software. This can be done by providing unexpected input to a web application, or by providing unexpected input to a binary.

## Wfuzz

[wfuzz](https://github.com/xmendez/wfuzz)

```bash
wfuzz --hw=153 -c -t 200 -w ~/Documents/Security/wordlists/common.txt http://40.121.87.195:60004/\?file\=..//FUZZ.txt
```

```bash
wfuzz -c --hh=3245 -w ~/Documents/Security/wordlists/common.txt -H "HOST: FUZZ.<URL>" http://<URL>
```

- `--hw` : Hide words with length equal to or less than the specified value
- `-c` : Show output in color
- `-t` : Number of threads
- `-w` : Wordlist to use
- `FUZZ` : Where the payload will be placed

## Wfpayload

Wfpayload is a tool that generates payloads for fuzzing.

In this case where we know the range of the payload we can use the following command to generate a payload.

```bash
wfpayload -z range --zD 0000-6000 > payload.txt
wfuzz -c --hw=31 --hc=404 -w payload.txt http://10.13.37.11/backups/backup_2024032823FUZZ.zip
```
