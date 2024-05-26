# Desktop Environment

Some desktop environments are exploitable or one of the libraries they use is.

One example could be the `enlightenment` desktop environment. It has a vulnerability that allows an attacker to execute arbitrary code with the privileges of the user running the enlightenment desktop environment.

## Finding

```shell
dpkg -l | grep -E 'gnome|kde|xfce|lxde|enlightenment'
```

## Links

- https://github.com/MaherAzzouzi/CVE-2022-37706-LPE-exploit