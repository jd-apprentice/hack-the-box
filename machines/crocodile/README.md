- Scans are in `fullport` files.
- `allowed` are the users for the `login` page.
- `feroxbuster` is used to discovery, along with the files in the `utils` folder (wordlists, etc).
- Results from `feroxbuster` are in the `discovery.txt` file.
- `links.txt` contains useful links.

1. Scan the machine with `nmap`
2. Enter via anonymous FTP
3. Download files from the FTP server
4. Use `feroxbuster` to discover routes
5. Login to the web server with the discovered credentials
6. Obtain your flag

https://www.hackthebox.com/achievement/machine/834305/404