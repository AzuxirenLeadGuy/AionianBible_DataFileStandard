# This file prepares the `Content.txt` file which is used as an index for downloads

import pathlib
cwd = str(pathlib.Path(__file__).parent.resolve())

import os

files = [x for x in os.listdir(cwd) if x.endswith('.noia')]
files.sort()

map = {}

for file in files:
    with open(f'{cwd}/{file}') as f:
        f.readline() # Ignore first line
        z = f.readline() # 
        assert z.startswith('# File Size:'), f"Invalid format! for file {file} having line {z}"
        z = int(z.split(':')[1])
        map[file] = z

# print(map)

with open(f'{cwd}/Content.txt', 'w+') as f:
    for key in map:
        value = map[key]
        f.write(f'{key}\t{value}\n')