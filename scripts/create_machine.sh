#!/bin/bash

folder_name=$1

if [ -z $folder_name ]; then
  echo "Please provide a folder name"
  exit 1
fi

mkdir -p machines/$folder_name
mkdir -p machines/$folder_name/assets/
mkdir -p machines/$folder_name/utils/
touch machines/$folder_name/README.md