import os
import sys
import hashlib
from collections import defaultdict

hash_to_files = defaultdict(list)
base_path = sys.argv[1]
for current_dir, _, files in os.walk(base_path):
    for filename in files:
        files_paths = os.path.join(current_dir, filename)
        if not (os.path.islink(files_paths) or
                filename.startswith(('.', '~'))):
            hash = hashlib.md5()
            with open(files_paths, 'rb') as file:
                hash.update(file.read())
            filename_hash = hash.hexdigest()
            hash_to_files[filename_hash].append(os.path.abspath(files_paths))
for hash_to_values in hash_to_files.values():
    if len(hash_to_values) > 1:
        print(':'.join(hash_to_values))
