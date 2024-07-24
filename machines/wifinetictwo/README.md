User FLAG
-----

1. Run nmap to find open ports
2. Find port 8080
3. Find the login page
4. OpenPLC app
5. default creds `openplc:openplc`
6. Go into `hardware` and modify the `blank` program
7. Add reverse shell code in C
8. Compile the code
9. Run the PLC
10. Get a reverse shell
11. Find the user flag in the root directory

Root FLAG
-----

1. Enumerate network interfaces
2. Find the `wlan0` interface with wireless capabilities
3. Scan `iwlist wlan0 s`
4. Obtain ESSID, Address
5. Crack with `reaver -i <interface> -b <access-point> -v`
6. Obtain password for WP2
7. Create `wpa_supplicant.conf` file `wpa_passphrase WLAN_NAME PASSWORD` > `wpa_supplicant.conf`
8. Connect to the network `wpa_supplicant -B -i wlan0 -c wpa_supplicant.conf`
9. Add a IP to the interface `ifconfig wlan0 192.168.1.200 netmask 255.255.255.0`
10. SSH into the network `ssh root@192.168.1.1`

## Links

- https://autonomylogic.com/docs/2-1-openplc-runtime-overview/
- https://github.com/izenynn/c-reverse-shell/blob/main/linux.c
- https://www.baeldung.com/linux/connect-network-cli
- https://www.kali.org/tools/reaver/