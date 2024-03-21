# Socat

Socat is a command line based utility that establishes two bidirectional byte streams and transfers data between them. Because of its versatility and ease of use, it is often used to create network connections between systems.

## Usage

In the target machine

```bash
socat TCP-LISTEN:<PORT>,reuseaddr,fork EXEC:<BINARY> & 
```

Where:

- `TCP-LISTEN` is the type of connection to create.
- `<PORT>` is the port number to expose.
- `reuseaddr` allows the port to be reused.
- `fork` allows the connection to be forked.
- `EXEC:<BINARY>` is the binary to execute.
- `&` runs the command in the background.

In your machine

```bash
nc <IP> <PORT>
```