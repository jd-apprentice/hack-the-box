# Whatweb

Whatweb is a web scanner that identifies what software is used for a website. It can recognize content management systems, blogging platforms, stats/analytics packages, JavaScript libraries, server software, and more.

## Usage

```bash
whatweb <URL>
```

```bash
whatweb jonathan.com.ar

http://jonathan.com.ar [301 Moved Permanently] Country[UNITED STATES][US], HTTPServer[cloudflare], IP[104.21.75.180], RedirectLocation[https://jonathan.com.ar/], UncommonHeaders[report-to,nel,cf-ray,alt-svc]

https://jonathan.com.ar/ [200 OK] Country[UNITED STATES][US], HTML5, HTTPServer[cloudflare], IP[104.21.75.180], Script, Title[/], UncommonHeaders[cf-cache-status,report-to,nel,cf-ray,alt-svc]
```