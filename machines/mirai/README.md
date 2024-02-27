User FLAG
-----

1. Scan ports
2. Try to do something with dnsmasq
3. Then with lighttpd
4. Scan headers with cURL
5. Find that page is runnning `pi-hole`
6. Search for default credentials of a raspberry pi
7. Login via SSH
8. Obtain user flag

Root FLAG
----
1. Since pi has root, go to /root/root.txt
2. Find that flag is not there
3. Follow trace
4. Found that flag is in memory
5. Use `strings` to find flag in the /dev/sdb
6. Obtain root flag

## Versions

OpenSSH 6.7p1 Debian 5+deb8u3 (protocol 2.0)
dnsmasq 2.76
lighttpd 1.4.35
X-Pi-hole

## Links

- https://www.howtogeek.com/427805/how-to-use-the-strings-command-on-linux/
- https://tutorials-raspberrypi.com/raspberry-pi-default-login-password/
- https://github.com/geeknik/the-nuclei-templates/blob/main/CVE-2014-2323.yaml