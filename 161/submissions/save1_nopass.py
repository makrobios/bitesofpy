import os

def traversing_tree(directory, files, dirs):
        with os.scandir(directory) as scan:
            for entry in scan:
                if entry.is_dir():
                    dirs += 1 
                    return traversing_tree(entry, files, dirs)
                files += 1 
        return (dirs, files)

def count_dirs_and_files(directory='.'):
    """Count the amount of of directories and files in passed in "directory" arg.
       Return a tuple of (number_of_directories, number_of_files)
    """
    files, dirs = (0, 0)
    return traversing_tree(directory, files, dirs)
    

print(count_dirs_and_files(directory='./test'))
