# Behind The Scenes

1. Download the binary and run it.

```bash
./behindthescenes

## We get this output
./challenge <password>
```

2. `Strings` command to see if we can find anything interesting.

```bash
strings behindthescenes

/lib64/ld-linux-x86-64.so.2
libc.so.6
strncmp
puts
__stack_chk_fail
printf
strlen
sigemptyset
memset
sigaction
__cxa_finalize
__libc_start_main
GLIBC_2.4
GLIBC_2.2.5
_ITM_deregisterTMCloneTable
__gmon_start__
_ITM_registerTMCloneTable
u+UH
[]A\A]A^A_
./challenge <password>
> HTB{%s}
:*3$"
GCC: (Ubuntu 9.3.0-17ubuntu1~20.04) 9.3.0
crtstuff.c
deregister_tm_clones
__do_global_dtors_aux
completed.8060
__do_global_dtors_aux_fini_array_entry
frame_dummy
__frame_dummy_init_array_entry
main.c
__FRAME_END__
__init_array_end
_DYNAMIC
__init_array_start
__GNU_EH_FRAME_HDR
_GLOBAL_OFFSET_TABLE_
__libc_csu_fini
strncmp@@GLIBC_2.2.5
_ITM_deregisterTMCloneTable
puts@@GLIBC_2.2.5
sigaction@@GLIBC_2.2.5
_edata
strlen@@GLIBC_2.2.5
__stack_chk_fail@@GLIBC_2.4
printf@@GLIBC_2.2.5
memset@@GLIBC_2.2.5
__libc_start_main@@GLIBC_2.2.5
__data_start
segill_sigaction
sigemptyset@@GLIBC_2.2.5
__gmon_start__
__dso_handle
_IO_stdin_used
__libc_csu_init
__bss_start
main
__TMC_END__
_ITM_registerTMCloneTable
__cxa_finalize@@GLIBC_2.2.5
.symtab
.strtab
.shstrtab
.interp
.note.gnu.property
.note.gnu.build-id
.note.ABI-tag
.gnu.hash
.dynsym
.dynstr
.gnu.version
.gnu.version_r
.rela.dyn
.rela.plt
.init
.plt.got
.plt.sec
.text
.fini
.rodata
.eh_frame_hdr
.eh_frame
.init_array
.fini_array
.dynamic
.data
.bss
.comment
```

We now know that the binary is named `challenge` and it takes a password as an argument.

```
./challenge <password>
> HTB{%s}
```

3. Open the binary in Cutter and decompile it.

```bash
cutter behindthescenes
```

Seeing the binary as hexadecimal shows the following 

```bash
010002002e2f6368616c6c656e6765203c70617373776f72643e0049747a005f306e004c795f00554432003e204854427b25737d
```

Now this in text is

```
  ./challenge <password> FLAG> HTB{%s}
```

Congratulations! You have found the flag.