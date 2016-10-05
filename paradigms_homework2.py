import os
import sys
import hashlib
from collections import defaultdict

hash_to_files = defaultdict(list)
base_path = sys.argv[1]
for current_dir, _, files in os.walk(base_path):
    for filename in files:
        path = os.path.join(current_dir, filename)
        if (not os.path.islink(path) and
                not filename.startswith('.', '~')):
            hash = hashlib.md5()
            with open(path, 'rb') as file:
                hash.update(file.read())
            file_hash = hash.hexdigest()
            hash_to_files[file_hash].append(os.path.abspath(files_paths))
for hash_to_file in hash_to_files.values():
    if len(hash_to_file) > 1:
        print(':'.join(hash_to_file))
