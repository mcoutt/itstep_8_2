def files(info):
    f = open('test.txt', 'a+')
    for i in info:
        f.write(i + '\n')
    f.close()
    a = open("test.txt")
    return print(a.read())


l = [str(i)+str(i+1) for i in range(10)]

b = "HEllo"
files(b)
files(l)




