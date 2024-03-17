# Networking

## Common

`ifconfig` - show network interfaces
`iwlist <interface> s` - scan the interface

### Add IP to interface

`ifconfig wlan0 192.168.1.200 netmask 255.255.255.0`

Where:

- `wlan0` is the interface
- `192.168.1` is the network and `200` is the IP. We have 254 IPs available
- `255.255.255.0` is the netmask

### Connect to a network

If we want to connect to a network, we can use `wpa_supplicant`:

```bash
wpa_passphrase WLAN_NAME PASSWORD > wpa_supplicant.conf
wpa_supplicant -B -i wlan0 -c wpa_supplicant.conf
```

Where:

- `WLAN_NAME` is the name of the network
- `PASSWORD` is the password
- `-B` runs in the background

## Links

- https://www.baeldung.com/linux/connect-network-cli