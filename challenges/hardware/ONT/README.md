```bash
files fwu_ver
fwu_ver: ASCII text
file hw_ver 
hw_ver: X1 archive data
file rootfs 
rootfs: Squashfs filesystem, little endian, version 4.0, zlib compressed, 10936182 bytes, 910 inodes, blocksize: 131072 bytes, created: Sun Oct  1 07:02:43 2023
```

Squashfs filesystem is a compressed read-only filesystem. We can extract the contents of the filesystem using `unsquashfs` tool.

```bash
unsquashfs <folder> rootfs
```

Now we can find the flag there

```bash
grep -r "HTB" folder
```