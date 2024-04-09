# Bash

With bash we can create scripts that automate tasks.

First we create a file withouth extension and add the following content:

```bash
#!/bin/bash

echo "Hello, World!"
```

Then we make the file executable:

```bash
chmod +x script
```

Finally we run the script:

```bash
./script
```

The output will be:

```bash
Hello, World!
```

If we want to make this executable from anywhere, we can move the file to a directory in the PATH:

```bash
sudo mv script /usr/local/bin
script
```