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
res, history = gen.send((999, 777,"history"))
print(res)
print(history)
