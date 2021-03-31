# Sources:  https://docs.python.org/3/library/hashlib.html
#           https://www.geeksforgeeks.org/sha-in-python/
#           https://stackoverflow.com/questions/22058048/hashing-a-file-in-python

import hashlib

def hashFile(fileName):
    hasher = hashlib.sha256()
    file = open(fileName, "rb")

    while True:
        chunk = file.read(hasher.block_size)
        if chunk:
            hasher.update(chunk)
        else:
            break

    return hasher.hexdigest()

def main():
    print(hashFile("hashinfunc.py"))

main()