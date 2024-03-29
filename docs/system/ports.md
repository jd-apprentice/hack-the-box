# Ports

Related to ports and how to interact with them.

## Check open ports

```bash
ss -tunl
netstat -tunl
```

## Port forwarding

[read](https://phoenixnap.com/kb/ssh-port-forwarding)

```bash
ssh -L <LOCAL_PORT>:<REMOTE_HOST>:<REMOTE_PORT> <USER>@<GATEWAY>
ssh -L 1111:127.0.0.1:8080 matthew@surveillance.htb
```

## Dump traffic

Here is an example of how to dump ICMP traffic on a specific interface, this can be used if we want to ping against our machine if we are running a XSS attack and test if the payload is working.

```bash
tcpdump -i tun0 -n icmp
```

Where each flag means:

- `-i` Listen on interface.
- `tun0` The interface to listen on.
- `-n` Don't convert addresses (i.e., host addresses, port numbers, etc.) to names.
- `icmp` Capture only ICMP traffic.

## 161 SNMP

SNMP is a protocol that allows for the monitoring of network-attached devices. It is commonly used to gather information about network devices, such as routers, switches, and servers.

### Enumeration

```bash
snmpwalk -c <COMMUNITY_STRING> <VERSION> <IP>
snmpwalk -c public -v1 10.13.37.11
snmpbulkwalk -c public -v1 10.13.37.11
```

Where each flag means:

- `-c` Community string.
- `public` Common community string.
- `-v` SNMP version.
- `1` SNMP version 1.

To obtain the community string, we can use the following command:

```bash
python3 snmpbrute.py -t 10.13.37.11 -f ~/Documents/Security/wordlists/common-snmp-community-strings-onesixtyone.txt
onesixtyone -c <WORDLIST> <IP>
onesixtyone -c /usr/share/wordlists/common-snmp-community-strings-onesixtyone.txt
Scanning 1 hosts, 121 communities
10.13.37.11 [public] Linux Leakage 4.15.0-72-generic #81-Ubuntu SMP Tue Nov 26 12:20:02 UTC 2019 x86_64
10.13.37.11 [public] Linux Leakage 4.15.0-72-generic #81-Ubuntu SMP Tue Nov 26 12:20:02 UTC 2019 x86_64
```