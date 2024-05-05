# Evil Win-RM

Evil-WinRM is the ultimate WinRM shell for hacking/pentesting.

## Installation

```bash
gem install evil-winrm
```

## Run with Docker

```bash
docker run --rm -ti --name evil-winrm -v /home/foo/ps1_scripts:/ps1_scripts -v /home/foo/exe_files:/exe_files -v /home/foo/data:/data oscarakaelvis/evil-winrm -i 192.168.1.100 -u Administrator -p 'MySuperSecr3tPass123!' -s '/ps1_scripts/' -e '/exe_files/'
```