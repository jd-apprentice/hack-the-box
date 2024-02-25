# Valentine

User FLAG
-----

1. Scan ports with nmap
2. Scan for vulnerabilities with nmap scripts
3. Discovery with dirsearch
4. Download `hype_key`
5. Use CVE-2014-0224 to obtain the hype_key password
6. SSH into the machine with the hype_key and `hype` user
7. Obtain the user flag

## Versions

Apache 2.2.22
PHP 5.3.10
SSH-2.0-OpenSSH_5.9p1 Debian-5ubuntu1.10

## CVEs

CVE-2011-1002
CVE-2014-0224 (This one)
CVE-2014-0160
CVE-2014-3566

## Links

- https://gist.github.com/RitamDey/128bb6dbfa6a7a1d753182341d57a9c7
- https://stackoverflow.com/questions/73795935/sign-and-send-pubkey-no-mutual-signature-supported
- https://docs.metasploit.com/docs/using-metasploit/getting-started/nightly-installers.html