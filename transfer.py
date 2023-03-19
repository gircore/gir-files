#!/usr/bin/env python3
import os
import sys
import glob
import shutil
import subprocess

source_folder = sys.argv[1]
destination_folder = os.path.abspath(sys.argv[2])
gir_list = sys.argv[3].split(',')

os.makedirs(destination_folder, exist_ok=True)

gir_files = []

for gir in gir_list:
  with open(gir) as file:
    gir_files.extend([tuple(line.rstrip().split(',')) for line in file])

for (file,pkg,maxversion) in gir_files:
  src = os.path.join(source_folder, file)
  dest = os.path.join(destination_folder, file)

  with subprocess.Popen(["pkg-config", "--exists", f"{pkg} <= {maxversion}"]) as proc:
    proc.communicate()
    if proc.returncode == 1:
      print(f"Skip new version of package {pkg}")
    else:
      try:
        shutil.copy(src, dest)
        print(f"Copied {src} to {dest}")
      except FileNotFoundError:
        print(f"Could not copy {src} to {dest}.")
        sys.exit(1)
