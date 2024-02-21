User FLAG
----

1. Scan ports
2. Open website
3. Inspect page
4. Enter blog route
5. Scan for files
6. Find software version
7. Search for exploit
8. Reverse shell
9. Find user flag in home directory

Notes
----

## Important

http://10.10.10.75/nibbleblog/admin/

Nibbleblog 4.0.3 "Coffee" ©2009 - 2014 | Developed by Diego Najar

- BASE_URL/nibbleblog/update.php
- personal.zip

## Scans

- `nmap -T4 --min-rate 5000 -sV -o open 10.10.10.75`
- `feroxbuster --insecure -u http://10.10.10.75/nibbleblog -o ferox -w ~/Documents/Security/wordlists/php.txt`

Root FLAG
-----

1. Check for `sudo -l` permissions
2. Locate the script that is being able to be run as root
3. Modify the script to obtain the root flag
4. Run the script to obtain the root flag
5. Congrats!

## Links
- https://github.com/dix0nym/CVE-2015-6967
- https://highon.coffee/blog/reverse-shell-cheat-sheet/#php-reverse-shell
- https://superuser.com/questions/98089/sending-file-via-netcat