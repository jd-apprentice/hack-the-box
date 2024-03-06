# SHC

Shell script compiler is a tool that compiles a script written in bash or sh to a binary file. This binary file can be executed on any system that has the same architecture as the system on which the script was compiled.

## Installation

### Debian/Ubuntu

```bash
sudo add-apt-repository ppa:neurobin/ppa
sudo apt-get update
sudo apt-get install shc
```

## Usage

```bash
shc -f script.sh -o script
```

Where:

- `-f` is the input file
- `-o` is the output file

After running the above command, a binary file named `script` will be created.

We can execute the binary file as follows:

```bash
./script
```

Or better we could move the binary file to a directory in the PATH and execute it from anywhere.

```bash
sudo mv script /usr/local/bin
script
```