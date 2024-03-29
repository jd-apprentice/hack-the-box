# Checksec

Checksec is a tool that can be used to check the security properties of a binary. It can be used to check for the presence of various security features such as NX, PIE, RELRO, and more.

## Usage

```bash
checksec --file=<binary>
```

## Example

```bash
checksec --file=behindthescenes
RELRO           STACK CANARY      NX            PIE             RPATH      RUNPATH      Symbols         FORTIFY Fortified       Fortifiable     FILE
Full RELRO      Canary found      NX enabled    PIE enabled     No RPATH   No RUNPATH   73) Symbols       No    0               2               behindthescenes
```