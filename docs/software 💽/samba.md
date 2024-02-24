# Samba

Samba is a free software re-implementation of the SMB/CIFS networking protocol. It allows file and print sharing between computers running Microsoft Windows and computers running Unix-like operating systems.

Ports: 139, 445

## smbclient

[docs](https://www.samba.org/samba/docs/current/man-html/smbclient.1.html)

```bash
smbclient \\\\<target-ip>\\<share-name>
```