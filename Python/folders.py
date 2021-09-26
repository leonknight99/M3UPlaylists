import os


def path_input():  # Error checking for user path input
    while True:
        folder_path = str(input('\nInsert path of folder: '))
        if os.path.isdir(folder_path):
            break
        print('Error: Incorrect path to a folder inserted')

    return folder_path


def set_leaf(tree, branches, leaf):
    """ Set a terminal element to *leaf* within nested dictionaries.              
    *branches* defines the path through dictionnaries.                            

    Example:                                                                      
    >>> t = {}                                                                    
    >>> set_leaf(t, ['b1','b2','b3'], 'new_leaf')                                 
    >>> print t                                                                   
    {'b1': {'b2': {'b3': 'new_leaf'}}}                                             
    """
    if len(branches) == 1:
        tree[branches[0]] = leaf
        return
    if not branches[0] in tree: #tree.has_key(branches[0]):
        tree[branches[0]] = {}
    set_leaf(tree[branches[0]], branches[1:], leaf)


def directory_to_tree(root_path):  # Some of this work was copied from a Stack Overflow post
    '''Creates a tree in the form of a dictionary of a selected directory names "root"
    '''
    root_name = os.path.basename(root_path)
    tree = {}
    for (path, dirs, files) in os.walk(root_path):
        branches = [root_name]
        if path != root_path:
            branches.extend(os.path.relpath(path, root_path).split('/'))

        set_leaf(tree, branches, dict([(d,{}) for d in dirs] + [(f,None) for f in files]))

    print(tree)


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


directory_to_tree('/Volumes/SANDISK128/Music/Loessless')