#!/usr/bin/env python3
import os
import sys
import glob
import shutil
import subprocess

source_folder = sys.argv[1]
destination_folder = os.path.abspath(sys.argv[2])
backup_folder = os.path.join(destination_folder, 'backup')
gir_list = sys.argv[3].split(',')

os.makedirs(destination_folder, exist_ok=True)
os.makedirs(backup_folder, exist_ok=True)

files_to_delete = glob.glob(os.path.join(backup_folder, "*"))
for f in files_to_delete:
  os.remove(f)
  print(f"Deleted {f}")

files_to_move = glob.glob(os.path.join(destination_folder, "*"))
for f in files_to_move:
  shutil.move(f, backup_folder)
  print(f"Moved {f} to {backup_folder}")

gir_files = []

for gir in gir_list:
  with open(gir) as file:
    gir_files.extend([tuple(line.rstrip().split(',')) for line in file])

for (file,pkg,nextversion) in gir_files:
  src = os.path.join(source_folder, file)
  dest = os.path.join(destination_folder, file)
  backup = os.path.join(backup_folder, file)

  with subprocess.Popen(["pkg-config", "--modversion", f"{pkg}"], stdout=subprocess.PIPE) as proc:
    stdout, stderr = proc.communicate()
    modversion = stdout.decode('UTF-8').rstrip()
    print(f"Found {pkg} version: {modversion} (must be lower than {nextversion})")

  with subprocess.Popen(["pkg-config", "--exists", '--print-errors', f"{pkg} < {nextversion}"]) as proc:
    proc.communicate()
    if proc.returncode == 1:
      src = backup
  
  try:
    shutil.copy(src, dest)
    print(f"Copied {src} to {dest}")
  except FileNotFoundError:
    print(f"Could not copy {src} to {dest}.")
    sys.exit(1)

files_to_delete = glob.glob(os.path.join(backup_folder, "*"))
for f in files_to_delete:
  os.remove(f)
  print(f"Deleted {f}")

os.rmdir(backup_folder)
print(f"Deleted {backup_folder}")


