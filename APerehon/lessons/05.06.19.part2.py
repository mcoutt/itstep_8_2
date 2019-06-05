a = 5

def f():
    a = 10
    def f1():
        global a
        print('f1 = ',a)
    def f2():
        nonlocal a
        a = a + 10
        print('f2',a)
    f2()
    f1()
    print('f = ',a)


f()
