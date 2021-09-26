import os

d = {}
d['folder1'] = {}
d['folder1']['ABBA'] = {}
d['folder1']['MJ'] = {}
d['folder1']['ABBA']['ABBA Gold'] = ['song 1', 'song 2']
d['folder1']['MJ']['best'] = ['song 1', 'song 2']
print(d)
d['folder1']['ABBA']['ABBA Gold'] = ['Mamma Mia', 'Waterloo']
print(d)