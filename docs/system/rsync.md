# Rsync

Rsync is a fast and versatile file copying tool that can be used to copy files from one host to another. It is a powerful tool that can be used to synchronize files between two directories, or to copy files from one host to another. Rsync is a great tool for backing up files, and it can be used to copy files from one host to another over a network.

## Default PORT

Rsync uses port 873 by default.

## Anonymous rsync

```bash
rsync --list-only 10.129.136.195::
```

## Download files

```bash
rsync 10.129.136.195::public/file.txt file.txt
```