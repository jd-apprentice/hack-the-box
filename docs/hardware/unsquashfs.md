# Unsquashfs

Unsquashfs is a tool that can extract files from a squashfs filesystem. It is part of the squashfs-tools package.

## Usage

To find if a file is a squashfs filesystem, use the `file` command.

```bash
file <file>
```

If we get the output as `Squashfs filesystem`, we can extract the contents of the filesystem using `unsquashfs` tool.

```bash
unsquashfs <folder> <file>
```

Then we can dig into the extracted folder to find the flag.

```bash
grep -r "HTB" <folder>
```