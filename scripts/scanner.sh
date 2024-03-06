#!/bin/bash
## Script to automate nmap scans
## Usage: sh nmap_scan.sh
### Mady by jd-apprentice

scan() {
    local target=$1
    local script_name=$2
    local args=$3
    zenity --info --text="Scanning $target with $script_name script and args: $args"
    nmap --script "$script_name"* "$args" "$target"
}

zenity --forms --title="Nmap Scan" --text="Enter the required information" \
 --add-entry="Target" --add-entry="Script" --add-entry="Args" > /tmp/nmap_scan.txt

target=$(awk -F'|' '{print $1}' /tmp/nmap_scan.txt)
script=$(awk -F'|' '{print $2}' /tmp/nmap_scan.txt)
args=$(awk -F'|' '{print $3}' /tmp/nmap_scan.txt)

if [ -z "$target" ] || [ -z "$script" ]; then
    zenity --error --text="Target and Script are required"
    exit 1
fi

scan "$target" "$script" "$args"
zenity --notification --text="Scan completed"