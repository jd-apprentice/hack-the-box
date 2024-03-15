# DNS

DNS (Domain Name System) is a system that translates domain names to IP addresses. It is a distributed database that contains records for every domain name on the internet.

## Locate

Whenever we have an IP address, we can use wget to find the domain name.

```bash
wget --server-response 10.10.11.194      
--2024-03-01 22:32:36--  http://10.10.11.194/
Connecting to 10.10.11.194:80... connected.
HTTP request sent, awaiting response... 
  HTTP/1.1 301 Moved Permanently
  Server: nginx/1.18.0 (Ubuntu)
  Date: Sat, 02 Mar 2024 01:32:37 GMT
  Content-Type: text/html
  Content-Length: 178
  Connection: keep-alive
  Location: http://soccer.htb/
Location: http://soccer.htb/ [following]
--2024-03-01 22:32:37--  http://soccer.htb/
Resolving soccer.htb (soccer.htb)... failed: Name or service not known.
wget: unable to resolve host address ‘soccer.htb’
```

Also sometimes `cURL` can be used to find the domain name.

```bash
curl -I <IP>  

HTTP/1.1 301 Moved Permanently
Server: nginx/1.18.0 (Ubuntu)
Date: Sat, 02 Mar 2024 01:27:24 GMT
Content-Type: text/html
Content-Length: 178
Connection: keep-alive
Location: http://soccer.htb/
```

If the port `53` is open we can also ddo something like

```bash
nslookup 10.10.10.29
29.10.10.10.in-addr.arpa        name = bank.htb.
```

Then with `dig` we can go deeper.

```bash
dig axfr bank.htb @10.10.10.29                                                                 

; <<>> DiG 9.18.18-0ubuntu0.22.04.2-Ubuntu <<>> axfr bank.htb @10.10.10.29
;; global options: +cmd
bank.htb.               604800  IN      SOA     bank.htb. chris.bank.htb. 2 604800 86400 2419200 604800
bank.htb.               604800  IN      NS      ns.bank.htb.
bank.htb.               604800  IN      A       10.10.10.29
ns.bank.htb.            604800  IN      A       10.10.10.29
www.bank.htb.           604800  IN      CNAME   bank.htb.
bank.htb.               604800  IN      SOA     bank.htb. chris.bank.htb. 2 604800 86400 2419200 604800
;; Query time: 184 msec
;; SERVER: 10.10.10.29#53(10.10.10.29) (TCP)
;; WHEN: Fri Mar 15 00:14:29 -03 2024
;; XFR size: 6 records (messages 1, bytes 171)
```

Once we have the domain name, we can add it to the `/etc/hosts` file.

```bash
sudo nano /etc/hosts

127.0.0.1       localhost
127.0.1.1       dyallo-MS-7A39
10.10.11.194    soccer.htb
10.10.10.29     bank.htb
```

Then when we access the ip address, we can see the website.