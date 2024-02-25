# Curl

curl is a command line tool to transfer data to or from a server.

## Send a request with payload

```bash
curl -X POST http://example.com -d '{"data": "value"}'
```

## Escape characters

```bash
curl -X POST http://example.com -d '{\"data\": \"value\"}'
```

## Send URL encoded data

```bash
curl -X POST http://example.com --data-urlencode 'data=value'
```

## Multi line command

```bash
curl -X POST http://example.com \
-d '{\"data\": \"value\"}' \
-H 'Content-Type: application/json' \
| jq
```