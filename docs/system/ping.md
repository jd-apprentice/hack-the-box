# Ping

Ping is a simple command that checks if the bot is online and responsive.

## Usage

```bash
# Basic usage
ping 10.13.37.11
PING 10.13.37.11 (10.13.37.11) 56(84) bytes of data.
64 bytes from 10.13.37.11: icmp_seq=1 ttl=63 time=248 ms

--- 10.13.37.11 ping statistics ---
1 packets transmitted, 1 received, 0% packet loss, time 0ms
rtt min/avg/max/mdev = 247.591/247.591/247.591/0.000 ms
# Record route
ping 10.13.37.11 -R
PING 10.13.37.11 (10.13.37.11) 56(124) bytes of data.
64 bytes from 10.13.37.11: icmp_seq=1 ttl=63 time=247 ms
RR:     10.10.14.4
        10.13.37.2
        10.13.37.11
        10.13.37.11
        10.10.14.1
        10.10.14.4
```

Where `icmp_seq` is the sequence number of the packet, `ttl` is the time to live, and `time` is the time it took for the packet to reach the destination.

When ttl is near 64, it means a the server is a linux server. When ttl is near 128, it means the server is a windows server.