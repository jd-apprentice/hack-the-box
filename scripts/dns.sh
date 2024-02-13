#!/bin/bash

domain=$1

itteration=0
for script in $(ls /usr/share/nmap/scripts/dns*); do
  echo "scanning with $script"
  nmap --script "$script" -oA scans/"$itteration"_script $1
  itteration=$((itteration+1))
done

rm scans/*.gnmap
rm scans/*.xml
echo "Scanning complete 🥳"