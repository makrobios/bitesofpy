import os

ONE_KB = 1024


def get_files(dirname, size_in_kb):
    """Return files in dirname that are >= size_in_kb"""
    for (dirpath, dirname, files) in os.walk(dirname):
        for file in files:
            if os.lstat(os.path.join(dirpath,file)).st_size >= size_in_kb * ONE_KB:
                yield file

print(list(get_files('.', 3)))