#!/usr/bin/env python3
import os
import sys
import shutil

source_folder = sys.argv[1]
destination_folder = sys.argv[2]

with open('gir_files.txt') as file:
  gir_files = [line.rstrip() for line in file]

for file in gir_files:
  src = os.path.join(source_folder, file)
  dest = os.path.join(os.path.abspath(destination_folder), file)
  try:
      shutil.copy(src, dest)
  except FileNotFoundError:
    print(f"Could not copy {file} to {dest_dir}.")
    sys.exit(1)