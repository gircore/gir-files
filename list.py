#!/usr/bin/env python3
import sys
import subprocess

# To run execute for example: 
# flatpak run --command=python3 --filesystem=home org.gnome.Sdk//46 list.py gir_files.txt,gir_files_linux.txt

gir_list = sys.argv[1].split(',')
gir_files = []

for gir in gir_list:
  with open(gir) as file:
    gir_files.extend([tuple(line.rstrip().split(',')) for line in file])

for (file,pkg,nextversion) in gir_files:
  with subprocess.Popen(["pkg-config", "--modversion", f"{pkg}"], stdout=subprocess.PIPE) as proc:
    stdout, stderr = proc.communicate()
    modversion = stdout.decode('UTF-8').rstrip()
    print(f"Found {pkg} version: {modversion} (must be lower than {nextversion})")