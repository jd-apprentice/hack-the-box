```
COMSPEC="C:\Windows\system32\cmd.exe"
CONTEXT_DOCUMENT_ROOT="/xampp/cgi-bin/"
CONTEXT_PREFIX="/cgi-bin/"
DOCUMENT_ROOT="C:/xampp/htdocs"
GATEWAY_INTERFACE="CGI/1.1"
HTTP_ACCEPT="text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8"
HTTP_ACCEPT_ENCODING="gzip, deflate"
HTTP_ACCEPT_LANGUAGE="en-US,en;q=0.5"
HTTP_CONNECTION="keep-alive"
HTTP_COOKIE="PHPSESSID=5f2hi37l4tk6ibbfjinn2lq2to"
HTTP_HOST="10.129.138.235"
HTTP_SEC_GPC="1"
HTTP_UPGRADE_INSECURE_REQUESTS="1"
HTTP_USER_AGENT="Mozilla/5.0 (X11; Linux x86_64; rv:123.0) Gecko/20100101 Firefox/123.0"
MIBDIRS="/xampp/php/extras/mibs"
MYSQL_HOME="\xampp\mysql\bin"
OPENSSL_CONF="/xampp/apache/bin/openssl.cnf"
PATH="C:\Windows\system32;C:\Windows;C:\Windows\System32\Wbem;C:\Windows\System32\WindowsPowerShell\v1.0\;C:\Windows\System32\OpenSSH\;C:\Users\svc_web\AppData\Local\Microsoft\WindowsApps"
PATHEXT=".COM;.EXE;.BAT;.CMD;.VBS;.VBE;.JS;.JSE;.WSF;.WSH;.MSC"
PHPRC="\xampp\php"
PHP_PEAR_SYSCONF_DIR="\xampp\php"
QUERY_STRING=""
REMOTE_ADDR="10.10.16.9"
REMOTE_PORT="59272"
REQUEST_METHOD="GET"
REQUEST_SCHEME="http"
REQUEST_URI="/cgi-bin/printenv.pl"
SCRIPT_FILENAME="C:/xampp/cgi-bin/printenv.pl"
SCRIPT_NAME="/cgi-bin/printenv.pl"
SERVER_ADDR="192.168.100.101"
SERVER_ADMIN="postmaster@localhost"
SERVER_NAME="10.129.138.235"
SERVER_PORT="80"
SERVER_PROTOCOL="HTTP/1.1"
SERVER_SIGNATURE="<address>Apache/2.4.52 (Win64) OpenSSL/1.1.1m PHP/8.1.1 Server at 10.129.138.235 Port 80</address>\n"
SERVER_SOFTWARE="Apache/2.4.52 (Win64) OpenSSL/1.1.1m PHP/8.1.1"
SYSTEMROOT="C:\Windows"
TMP="\xampp\tmp"
WINDIR="C:\Windows"
```

## Whatweb

```bash
http://10.129.138.235 [302 Found] Apache[2.4.52], Cookies[PHPSESSID], Country[RESERVED][ZZ], HTTPServer[Apache/2.4.52 (Win64) OpenSSL/1.1.1m PHP/8.1.1], IP[10.129.138.235], OpenSSL[1.1.1m], PHP[8.1.1], RedirectLocation[http://10.129.138.235/?file=mist], X-Powered-By[PHP/8.1.1]
http://10.129.138.235/?file=mist [200 OK] Apache[2.4.52], Cookies[PHPSESSID], Country[RESERVED][ZZ], HTTPServer[Apache/2.4.52 (Win64) OpenSSL/1.1.1m PHP/8.1.1], IP[10.129.138.235], MetaGenerator[pluck 4.7.18], OpenSSL[1.1.1m], PHP[8.1.1], Pluck-CMS[4.7.18], Title[Mist - Mist], X-Powered-By[PHP/8.1.1]
```

## Versions

- pluck 4.7.18
- TinyMCE 4

## Links

- https://www.exploit-db.com/exploits/49909
- https://www.exploit-db.com/exploits/51592
- https://gist.github.com/korrosivesec/a339e376bae22fcfb7f858426094661e