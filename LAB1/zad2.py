import os

def list_files(path, i=0):

    dirs = os.listdir(path)

    for dir in dirs:
        pad = i * "\t"
        print(pad + dir)
        try:
            list_files(path + "\\" + dir, i+1)
        except NotADirectoryError:
            continue

path = r"C:\Users\student\Documents\arzep"

print(list_files(path))