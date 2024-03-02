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

Once we have the domain name, we can add it to the `/etc/hosts` file.

```bash
sudo nano /etc/hosts

127.0.0.1       localhost
127.0.1.1       dyallo-MS-7A39
10.10.11.194    soccer.htb
```

Then when we access the ip address, we can see the website.
