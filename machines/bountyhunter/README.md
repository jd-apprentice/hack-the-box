User FLAG
-----

1. Scan ports
2. Check in deep obtained ports
3. Explore the webpage
4. Found endpoint that sends a POST request
5. Verify network of that endpoint
6. File `tracker_diRbPr00f314.php` is sending a payload called `data` with a base64
7. Decode the base64 and found a XML file
8. Modify the XML file to read `/etc/passwd`
9. Found development user
10. feroxbuster to find hidden files
11. found `db.php` file
12. Modify the XML file to read `db.php`
13. Decode the base64 and found credentials for the database and the user `development`
14. SSH with the user `development`
15. Found the user flag

If you want you can also use the `exploit.sh` and play around.

Root FLAG
-----

1. Do a simple `sudo -l` and found a file under /opt/skytrain_inc
2. Analyze the file and found that it is a python script
3. Create a crafted .md file under `/tmp` and execute the script with `sudo`
4. Crafted md should contain 

5. Start with `# Skytrain Inc`
6. `## Ticket to <Location>`
7. `__Ticket Code:__`
8. `**`
9. Until the first `+` must be an int that when divided by 7 has a remainder of 4

```md
# Skytrain Inc
## Ticket to New York

__Ticket Code:__
**32+100+43+ __import__('os').system('/bin/bash')**
```

10. Obtain root access
11. Found the root flag

## Versions

Apache 2.4.41
OpenSSH 8.2p1 Ubuntu

## Links

- https://stackoverflow.com/questions/296536/how-to-urlencode-data-for-curl-command
- https://medium.com/@minimalist.ascent/reading-local-files-with-xxe-exploit-c7fd91898754
- https://github.com/payloadbox/xxe-injection-payload-list