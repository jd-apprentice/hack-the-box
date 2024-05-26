# Checklist

This is a checklist of steps on what you should be looking at once you are inside a machine. This is not a definitive list, but it should give you a good idea of what to look for.

1. **Check for sudo privileges**
    ```shell
    sudo -l
    ```
2. **Check for environment variables**
    ```shell
    env
    ```
3. **Check for files with `setuid` bit set**
    ```shell
    find / -perm -4000 -type f 2>/dev/null
    ```
4. **Check for logs**
    ```shell
    cat /var/log/auth.log
    ```
5. **Check for cron jobs**
    ```shell
    cat /etc/crontab
    ```
6. **List running processes**
    ```shell
    ps aux
    ```
7. **Info about me**
    ```shell
    id || (whoami && groups) 2>/dev/null
    ```
8. **Check for writable files**
    ```shell
    find / -writable -type f 2>/dev/null
    ```

9. **Check for emails**
    ```shell
    cat /var/mail/$USER
    ```
10. **Check for network connections**
    ```shell
    netstat -tulnp
    ```
    
11. **Scan with `linpeas`**
    ```shell
    ./linpeas.sh
    ```
