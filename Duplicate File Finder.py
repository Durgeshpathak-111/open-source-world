import os
import hashlib

def file_hash(path):
    hasher = hashlib.md5()
    with open(path, 'rb') as f:
        buf = f.read()
        hasher.update(buf)
    return hasher.hexdigest()

def find_duplicates(directory):
    seen = {}
    for root, _, files in os.walk(directory):
        for file in files:
            path = os.path.join(root, file)
            h = file_hash(path)
            if h in seen:
                print(f"🔁 Duplicate found: {path} == {seen[h]}")
            else:
                seen[h] = path

if __name__ == "__main__":
    find_duplicates(".")
