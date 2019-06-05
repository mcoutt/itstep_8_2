a = ['1r2', '1a1', '1b0', '2a6', '2a2']
print(sorted(a))

print(sorted(a, key=lambda item: item[0] + item[-1]))
