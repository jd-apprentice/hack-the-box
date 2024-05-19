# Nikto

Nikto is a web server scanner that tests web servers for dangerous files/CGIs, outdated server software, and other problems. It performs generic and server type specific checks. It also captures and prints any cookies received.

## Installation

```shell
git clone https://github.com/sullo/nikto
# Main script is in program/
cd nikto/program
```

## Usage

```shell
# Run using the shebang interpreter
./nikto.pl -h http://10.13.38.11
+ Target IP:          10.13.38.11
+ Target Hostname:    10.13.38.11
+ Target Port:        80
+ Start Time:         2024-05-18 20:35:04 (GMT-3)
---------------------------------------------------------------------------
+ Server: Microsoft-IIS/10.0
+ /: The X-Content-Type-Options header is not set. This could allow the user agent to render the content of the site in a different fashion to the MIME type. See: https://www.netsparker.com/web-vulnerability-scanner/vulnerabilities/missing-content-type-header/
+ No CGI Directories found (use '-C all' to force check all possible dirs)
+ OPTIONS: Allowed HTTP Methods: OPTIONS, TRACE, GET, HEAD, POST .
+ OPTIONS: Public HTTP Methods: OPTIONS, TRACE, GET, HEAD, POST .
+ No creds found for realm 'COMPATIBILITY'
+ /.DS_Store: Apache on Mac OSX will serve the .DS_Store file, which contains sensitive information. Configure Apache to ignore this file or upgrade to a newer version. See: http://cve.mitre.org/cgi-bin/cvename.cgi?name=CVE-2001-1446
2+ 8254 requests: 0 error(s) and 4 item(s) reported on remote host
+ End Time:           2024-05-18 21:07:39 (GMT-3) (1955 seconds)
```