import hashlib
import time
import os

def compute_hash(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except FileNotFoundError:
        return None

def monitor_files(file_paths, interval=60):
    file_hashes = {file: compute_hash(file) for file in file_paths}

    while True:
        time.sleep(interval)
        for file in file_paths:
            current_hash = compute_hash(file)
            if current_hash != file_hashes[file]:
                print(f"[!] Change detected in {file}")
                file_hashes[file] = current_hash

if __name__ == "__main__":
    files_to_monitor = [
        "/path/to/important_file1.txt",
        "/path/to/important_file2.conf"
    ]
    monitor_files(files_to_monitor, interval=300)
