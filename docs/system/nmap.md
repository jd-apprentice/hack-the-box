# Nmap

Nmap is a network scanner that can be used to discover hosts and services on a computer network.

## Usage

```shell
nmap -p- -T4 <IP> -oA fullport --min-rate 5000
```

- `-p-` : Scan all ports
- `-T4` : Set the timing template to 4 (aggressive)
- `-oA` : Output in all formats
- `--min-rate` : Send packets at a minimum rate of 5000 per second
- `sV` : Probe open ports to determine service/version info
- `--open` : Only show open ports

## Scripts for NMAP

```shell
nmap --script dns-brute <IP>
```

- `dns-brute` : Brute force subdomains

## Vulnerability scanning

```shell
nmap --script vuln -o vul <IP>
```

## Location of NMAP scripts

```shell
ls /usr/share/nmap/scripts/
```
### Script redis

https://book.hacktricks.xyz/network-services-pentesting/6379-pentesting-redis

```shell
nmap --script redis-info -p 6379 <IP>
```

## etc/hosts

If there is a web server running on port 80, you can add the IP and domain to the `/etc/hosts` file.

```shell
echo "<IP> <domain>" >> /etc/hosts
```

Sometimes to obtain the dns name of the machine, you can use the following command.

```shell
curl -I <IP>
```

## Example

```shell
# Nmap 7.80 scan initiated Wed Feb 21 22:41:17 2024 as: nmap -T4 --min-rate 5000 -sV -o all 10.10.10.165
Nmap scan report for 10.10.10.165 (10.10.10.165)
Host is up (0.25s latency).
Not shown: 998 filtered ports
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.9p1 Debian 10+deb10u1 (protocol 2.0)
80/tcp open  http    nostromo 1.9.6
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel
```

### Cheatsheet

[stationx](https://www.stationx.net/nmap-cheat-sheet/)