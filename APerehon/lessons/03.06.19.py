a = [1, 2, 3, '4']

b = [str(i) for i in a]
c = list(map(str, a))
d = list((str(i) for i in a))
print('b =', b)
print('c =', c)
print('d =', d)

for i in c:
    print(i)

for i in d:
    print(i)
print('--------------------------------------')

for i in c:
    print(i)

for i in d:
    print(i)

word = 'mamapapa'
a = {}
# for letter in word:
#     try:
#         a[letter] += 1
#     except:
#         a[letter] = 1#создаем ключ с значением 1
#


while word:
    let = word[0]
    a[let] = word.count(let)
    print(word)
    word = word.replace(let,'')

print(a)

