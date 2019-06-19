# from os import listdir
# from os.path import isfile
# from os.path import join as joinpath
#
#
# files = listdir(".")

'''
my_txt = filter(lambda x: x.endswith('.txt'), files)
for i in my_txt:
    print(i)
'''

a = ['1r2', '1a1', '1b0', '2a6', '2a2']
print(a)
print(sorted(a))

print(sorted(a, key=lambda item: item[0] + item[-1]))

print(a.sort())
a.sort()
print(a)
