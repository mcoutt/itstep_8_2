def f():
    history = []
    a, b, command = yield None
    while command:
        tmp = a + b
        history.append((a, b, tmp))
        if command and command == "history":
            a, b, command = yield tmp, history
        else:
            a, b, command = yield tmp


gen = f()
next(gen)
res, his = gen.send((5, 5, "history"))
print(res)
print(his)
res = gen.send((4, 10, "g"))
print(res)
res, history = gen.send((999, 777, "history"))
print(res)
print(history)



# def f():
#     start = 0
#     end = 5
#     point = start
#     while True:
#         while point < end:
#             yield point
#             point += 1
#         while point > start:
#             yield point
#             point -=1
# import time
# a = f()
#
# while True:
#     print(next(a))
#     time.sleep(0.3)




def f():
    start,end = yield
    point = start
    while True:
        while point < end:
            data =yield point
            if data is not None:
                start,end = data
                point = start
                continue
            point += 1
        while point > start:
            data = yield point
            if data is not None:
                start,end = data
                point = start
                continue

            point -=1
import time
import random as R
gen = f()
next(gen)
print(gen.send((1,4)))
while True:
    a = R.randint(0,10)
    if a == 3:
        start,end = (map(int, input("->").split()))
        point = gen.send((start,end))
    else:
        point = next(gen)
    print(point)
    time.sleep(0.3)





