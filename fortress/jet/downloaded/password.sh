#!/bin/bash

for password in $(cat ./xortool_out/filename-key.csv); do
    echo $password
    unzip -P $password exploitme.zip
done