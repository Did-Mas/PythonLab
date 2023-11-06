import os


def count_files(path, recursive=False):
    dirs = os.listdir(path)

    nmb_of_dirs = len(dirs)

    if recursive:
        for dir in dirs:
            try:
                nmb_of_dirs += count_files(path + "\\" + dir, True)
            except NotADirectoryError:
                continue

    return nmb_of_dirs


path = r"C:\Users\student\Documents\arzep"

print(count_files(path, True))