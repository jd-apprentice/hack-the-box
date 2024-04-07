# Nmap

Nmap is a network scanner that can be used to discover hosts and services on a computer network.

## Usage

```shell
nmap -p- -T4 <IP> -oA fullport --min-rate 5000
sudo nmap -sU --open -T4 --top-ports 1000 -o udp 10.13.37.11
nmap -sUCV -p161 10.13.37.11 -oN udpscan
```

- `-p-` : Scan all ports
- `-T4` : Set the timing template to 4 (aggressive)
- `-oA` : Output in all formats
- `--min-rate` : Send packets at a minimum rate of 5000 per second
- `sV` : Probe open ports to determine service/version info
- `--open` : Only show open ports

## UDP

```shell
sudo nmap -sU --open -T4 --top-ports 1000 -o udp <IP>
```

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

### Cheatsheet

[stationx](https://www.stationx.net/nmap-cheat-sheet/)