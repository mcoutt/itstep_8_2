from os import listdir
from os.path import isfile
from os.path import join as joinpath


files = listdir(".")

mytxt = filter(lambda x: x.endswith('.txt'), files)
for i in mytxt:
    print(i)
