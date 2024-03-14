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