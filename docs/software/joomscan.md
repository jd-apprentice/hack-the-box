# Joomscan

Joomscan is a tool used to scan Joomla websites for vulnerabilities.

## Usage

```bash
joomscan -u http://10.10.11.3 
    ____  _____  _____  __  __  ___   ___    __    _  _ 
   (_  _)(  _  )(  _  )(  \/  )/ __) / __)  /__\  ( \( )
  .-_)(   )(_)(  )(_)(  )    ( \__ \( (__  /(__)\  )  ( 
  \____) (_____)(_____)(_/\/\_)(___/ \___)(__)(__)(_)\_)
			(1337.today)
   
    --=[OWASP JoomScan
    +---++---==[Version : 0.0.7
    +---++---==[Update Date : [2018/09/23]
    +---++---==[Authors : Mohammad Reza Espargham , Ali Razmjoo
    --=[Code name : Self Challenge
    @OWASP_JoomScan , @rezesp , @Ali_Razmjo0 , @OWASP

Processing http://10.10.11.3 ...



[+] FireWall Detector
[++] Firewall not detected

[+] Detecting Joomla Version
[++] Joomla 4.2.7

[+] Core Joomla Vulnerability
[++] Target Joomla core is not vulnerable

[+] Checking Directory Listing
[++] directory has directory listing : 
http://10.10.11.3/administrator/components
http://10.10.11.3/administrator/modules
http://10.10.11.3/administrator/templates
http://10.10.11.3/images/banners


[+] Checking apache info/status files
[++] Readable info/status files are not found

[+] admin finder
[++] Admin page : http://10.10.11.3/administrator/

[+] Checking robots.txt existing
[++] robots.txt is found
path : http://10.10.11.3/robots.txt 

Interesting path found from robots.txt
http://10.10.11.3/joomla/administrator/
http://10.10.11.3/administrator/
http://10.10.11.3/api/
http://10.10.11.3/bin/
http://10.10.11.3/cache/
http://10.10.11.3/cli/
http://10.10.11.3/components/
http://10.10.11.3/includes/
http://10.10.11.3/installation/
http://10.10.11.3/language/
http://10.10.11.3/layouts/
http://10.10.11.3/libraries/
http://10.10.11.3/logs/
http://10.10.11.3/modules/
http://10.10.11.3/plugins/
http://10.10.11.3/tmp/


[+] Finding common backup files name
[++] Backup files are not found

[+] Finding common log files name
[++] error log is not found

[+] Checking sensitive config.php.x file
[++] Readable config files are not found
```