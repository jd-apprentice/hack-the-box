#!/bin/bash
## Script to automate nmap scans
## Usage: sh nmap_scan.sh <target> <script>
### Mady by jd-apprentice

target=$1
script=$2

if [ -z $target ] || [ -z $script ]; then
    echo "Usage: sh nmap_scan.sh <target> <script>"
    exit 1
fi

scan() {
    local target=$1
    local script_name=$2
    local ports=$3
    nmap --script $script_name* -p $ports -o scans/$script_name $target
}

scan $target $script 445
echo "Scan $script done 🚀 saved on scans/$script"