#!/usr/bin/env python3
import os
import sys
import glob
import shutil

source_folder = sys.argv[1]
destination_folder = os.path.abspath(sys.argv[2])

files_to_delete = glob.glob(os.path.join(destination_folder, "*"))
for f in files_to_delete:
    os.remove(f)
    print(f"Deleted {f}")

with open('gir_files.txt') as file:
  gir_files = [line.rstrip() for line in file]

for file in gir_files:
  src = os.path.join(source_folder, file)
  dest = os.path.join(destination_folder, file)
  try:
      shutil.copy(src, dest)
      print(f"Copied {src} to {dest}")
  except FileNotFoundError:
    print(f"Could not copy {file} to {dest_dir}.")
    sys.exit(1)