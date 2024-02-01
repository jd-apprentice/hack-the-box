#!/bin/bash

folder_name=$1
is_machine=$2

create_directories_and_files() {
  local base_path=$1

  mkdir -p "$base_path/$folder_name"
  mkdir -p "$base_path/$folder_name/assets/"
  mkdir -p "$base_path/$folder_name/utils/"
  touch "$base_path/$folder_name/README.md"
}

if [ -z "$folder_name" ]; then
  echo "Please provide a folder name"
  exit 1
fi

if [ -z "$is_machine" ]; then
  create_directories_and_files "sherlocks"
  exit 0
fi
  
create_directories_and_files "machines"
echo "Done 🥳"