# Apachetomcatscanner

Apachetomcatscanner is a tool that can be used to scan Apache Tomcat servers for vulnerabilities.

## Usage

```bash
apachetomcatscanner -h
```

```bash
apachetomcatscanner -tt <target-ip> -tp <target-port>
apachetomcatscanner -tt <target-ip> -tp - ## All ports
apachetomcatscanner -tt <target-ip> -tp - --list-cves ## List possible CVEs on all ports
```