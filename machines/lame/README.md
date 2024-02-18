# Lame

User FLAG && Root FLAG
----

Primero empezamos con un mapeo de puertos

```shell
# Nmap 7.80 scan initiated Sun Feb 18 19:49:20 2024 as: nmap -p1-1000 -sV -Pn -T4 --min-rate 5000 -vvv -o version_full 10.10.10.3
Nmap scan report for 10.10.10.3 (10.10.10.3)
Host is up, received user-set (0.25s latency).
Scanned at 2024-02-18 19:49:21 -03 for 13s
Not shown: 996 filtered ports
Reason: 996 no-responses
PORT    STATE SERVICE     REASON  VERSION
21/tcp  open  ftp         syn-ack vsftpd 2.3.4
22/tcp  open  ssh         syn-ack OpenSSH 4.7p1 Debian 8ubuntu1 (protocol 2.0)
139/tcp open  netbios-ssn syn-ack Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
445/tcp open  netbios-ssn syn-ack Samba smbd 3.X - 4.X (workgroup: WORKGROUP)
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Read data files from: /usr/bin/../share/nmap
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sun Feb 18 19:49:34 2024 -- 1 IP address (1 host up) scanned in 13.92 seconds
```

De lo cual obtenemos un ftp el cual vamos a ver si podemos logear por anonymous login.

Pudimos logear por ftp pero no encontramos nada util.

Ahora vamos a ver por `telnet` la version de SSH 

```shell
telnet <IP> 22
```

Obtuvimos la version `SSH-2.0-OpenSSH_4.7p1 Debian-8ubuntu1`
No encontre ninguna vulnerabilidad para esta version.

Investigando por el nombre de netbios-ssn para el 139 y 445 no me llevo a ningun lado.

Volviendo a investigar sobre lo de FTP encontre un CVE el cual es el 2011-2523, el cual es un backdoor para vsftpd 2.3.4, el cual es la version que tiene el ftp, pero por lo visto al tener el puerto 6200 filtrado no funciona este CVE, descartando por completo FTP y SSH, ahora en vez de buscar por netbios voy a buscar con el nombre de samba.

Despues de buscar sobre la version de samba, encontre el CVE-2007-2447. A eso encontre un exploit en [github](https://github.com/amriunix/CVE-2007-2447)

Con lo cual podemos obtener un reverse shell y de ahi encontrar amblas flags sea user como root, una esta en el usuario makis y otra en la carpeta root.

Felicidades, encontraste ambas flags.

## Links
https://book.hacktricks.xyz/network-services-pentesting/137-138-139-pentesting-netbios
https://github.com/padsalatushal/CVE-2011-2523
https://github.com/amriunix/CVE-2007-2447