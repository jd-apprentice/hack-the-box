#!/bin/bash

folder_name=$1

create_directories_and_files() {
  local base_path=$1

  mkdir -p "$base_path/$folder_name"
  mkdir -p "$base_path/$folder_name/scripts/"
  mkdir -p "$base_path/$folder_name/scans/"
  touch "$base_path/$folder_name/README.md"
}

if [ -z "$folder_name" ]; then
  echo "Please provide a folder name"
  exit 1
fi
  
create_directories_and_files "machines"
echo "Done 🥳"