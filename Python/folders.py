import os


def path_input():  # Error checking for user path input
    while True:
        folder_path = str(input('\nInsert path of folder: '))
        if os.path.isdir(folder_path):
            break
        print('Error: Incorrect path to a folder inserted')

    return folder_path


def directory_to_dictionary(folder_path):  # Work in progress
    for (root, subDirectories, files) in os.walk(folder_path):
        print(root)
        print(subDirectories)
        print(files)
        print('-----------------------')


def compare_folders():  # Work in progress
    while True:
        nFolders = input('\nEnter number of folders to compare: ')
        if nFolders.isnumeric():
            nFolders = int(nFolders)
            break
        print('Error: A positive interger has not been entered')
    
    pathToFolders = [path_input() for n in range(nFolders)]
    for p in pathToFolders:
        print(os.walk(p))


directory_to_dictionary('/Volumes/SANDISK128/Music/Loessless')