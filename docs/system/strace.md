# Strace

Strace is a diagnostic, debugging and instructional userspace utility for Linux.

## Usage
    
```bash
strace mks
execve("/usr/local/bin/mks", ["mks"], 0x7fffec0e73b0 /* 100 vars */) = 0
prlimit64(0, RLIMIT_STACK, NULL, {rlim_cur=8192*1024, rlim_max=RLIM64_INFINITY}) = 0
prlimit64(0, RLIMIT_STACK, {rlim_cur=16384*1024, rlim_max=RLIM64_INFINITY}, NULL) = 0
rt_sigaction(SIGSEGV, {sa_handler=0x1006630, sa_mask=[], sa_flags=SA_RESTORER|SA_RESTART|SA_RESETHAND|SA_SIGINFO, sa_restorer=0x10073b0}, NULL, 8) = 0
rt_sigaction(SIGILL, {sa_handler=0x1006630, sa_mask=[], sa_flags=SA_RESTORER|SA_RESTART|SA_RESETHAND|SA_SIGINFO, sa_restorer=0x10073b0}, NULL, 8) = 0
rt_sigaction(SIGBUS, {sa_handler=0x1006630, sa_mask=[], sa_flags=SA_RESTORER|SA_RESTART|SA_RESETHAND|SA_SIGINFO, sa_restorer=0x10073b0}, NULL, 8) = 0
rt_sigaction(SIGFPE, {sa_handler=0x1006630, sa_mask=[], sa_flags=SA_RESTORER|SA_RESTART|SA_RESETHAND|SA_SIGINFO, sa_restorer=0x10073b0}, NULL, 8) = 0
rt_sigaction(SIGPIPE, {sa_handler=0x1005db0, sa_mask=[], sa_flags=SA_RESTORER, sa_restorer=0x10073b0}, NULL, 8) = 0
mmap(NULL, 4096, PROT_READ|PROT_WRITE, MAP_PRIVATE|MAP_ANONYMOUS, -1, 0) = 0x7feab493e000
write(2, "\n", 1
)                       = 1
write(2, " \342\226\210\342\226\210\342\226\210\342\226\204 \342\226\204\342\226\210\342\226\210\342\226\210\342\226\223 \342\226"..., 527 ███▄ ▄███▓ ██ ▄█▀  ██████ 
 ▓██▒▀█▀ ██▒ ██▄█▒ ▒██    ▒ 
 ▓██    ▓██░▓███▄░ ░ ▓██▄   
 ▒██    ▒██ ▓██ █▄   ▒   ██▒
 ▒██▒   ░██▒▒██▒ █▄▒██████▒▒
 ░ ▒░   ░  ░▒ ▒▒ ▓▒▒ ▒▓▒ ▒ ░
 ░  ░      ░░ ░▒ ▒░░ ░▒  ░ ░
 ░      ░   ░ ░░ ░ ░  ░  ░  
    ░   ░  ░         ░) = 527
write(2, "\n", 1
)                       = 1
write(2, "\nSkaffolding utility to create a"..., 68
Skaffolding utility to create a simple structure for htb machines.
) = 68
write(2, "Made by jd-apprentice\n", 22Made by jd-apprentice
) = 22
write(2, "\n", 1
)                       = 1
write(2, "Usage: mks <folder_name>\n", 25Usage: mks <folder_name>
) = 25
exit(1)                                 = ?
+++ exited with 1 +++
```

This is a simple example of how to use strace. It will show you all the system calls that the program makes.