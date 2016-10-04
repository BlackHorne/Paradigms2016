import os
import sys
import hashlib

from collections import defaultdict
hashsum_and_filenames = defaultdict(list)
hashsum_and_filenames_path = defaultdict(list)
base_path = sys.argv[1]
for actual_direct, include_direct, files in os.walk(base_path):
    for filename in files:
        filename_path = os.path.join(actual_direct, filename)
        if not (os.path.islink(filename_path) or (filename[0] == '.') or (filename[0] == '~')):
            symvols = hashlib.md5()
            with open(filename_path, 'rb') as file:
                symvols.update(file.read())
            filename_hashsum = symvols.hexdigest()
            hashsum_and_filenames[filename_hashsum].append(filename)
            hashsum_and_filenames_path[filename_hashsum].append(filename_path)
for iterator in hashsum_and_filenames:
    if len(hashsum_and_filenames[iterator]) > 1:
        print(':' .join(hashsum_and_filenames_path[iterator]))