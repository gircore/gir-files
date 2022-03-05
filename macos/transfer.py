#!/usr/bin/env python3
import os
import shutil

with open('gir_files.txt') as file:
  gir_files = [line.rstrip() for line in file]

dest_dir = os.path.abspath("./macos")

for file in gir_files:
  src = f"/usr/local/share/gir-1.0/{file}"
  dest = f"{dest_dir}/{file}"
  try:
      shutil.copy(src, dest)
  except FileNotFoundError:
    print(f"Could not copy {file} to {dest_dir}.")
    sys.exit(1)