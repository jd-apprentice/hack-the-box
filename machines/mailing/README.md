```shell
http://mailing.htb [200 OK] Country[RESERVED][ZZ], HTML5, HTTPServer[Microsoft-IIS/10.0], IP[10.129.56.156], Microsoft-IIS[10.0], PHP[8.3.3,], Title[Mailing], X-Powered-By[PHP/8.3.3, ASP.NET]
```

```bash
./exiftool $HOME/Documents/Proyectos/hack-the-box/machines/mailing/files/johnsmith.jpg 
ExifTool Version Number         : 12.84
File Name                       : johnsmith.jpg
Directory                       : /home/dyallo/Documents/Proyectos/hack-the-box/machines/mailing/files
File Size                       : 6.1 MB
File Modification Date/Time     : 2024:05:04 16:33:23-03:00
File Access Date/Time           : 2024:05:04 16:33:40-03:00
File Inode Change Date/Time     : 2024:05:04 16:33:23-03:00
File Permissions                : -rw-rw-r--
File Type                       : JPEG
File Type Extension             : jpg
MIME Type                       : image/jpeg
JFIF Version                    : 1.01
Resolution Unit                 : inches
X Resolution                    : 300
Y Resolution                    : 300
Current IPTC Digest             : 3c7a879125ea0496f5cea9aef811043c
Original Transmission Reference : 53616c7465645f5fab215e637899d0ac560d2732d50efff408eed2760d4cc9c5b0fcecde64aa349b
Application Record Version      : 4
Image Width                     : 4704
Image Height                    : 2823
Encoding Process                : Baseline DCT, Huffman coding
Bits Per Sample                 : 8
Color Components                : 3
Y Cb Cr Sub Sampling            : YCbCr4:4:4 (1 1)
Image Size                      : 4704x2823
Megapixels                      : 13.3
```

```bash
docker run --rm -ti --name evil-winrm -v /home/foo/ps1_scripts:/ps1_scripts -v /home/foo/exe_files:/exe_files -v /home/foo/data:/data oscarakaelvis/evil-winrm -i 192.168.1.100 -u Administrator -p 'MySuperSecr3tPass123!' -s '/ps1_scripts/' -e '/exe_files/'
```