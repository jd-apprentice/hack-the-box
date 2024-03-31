# Javascript

## Eval

The `eval` function is used to execute JavaScript code represented as a string. It is not recommended to use `eval` because it can introduce security vulnerabilities.

```javascript
eval('console.log("Hello, World!")');
// Hello, World!
```

We could do something like

```javascript
eval('require("fs").readFileSync("/etc/passwd").toString()');
```