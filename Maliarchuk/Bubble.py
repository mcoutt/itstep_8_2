def bubbleSort(list):
    for num in range(len(list) - 1, 0, -1):
        for i in range(num):
            if list[i] > list[i + 1]:
                pos = list[i]
                list[i] = list[i + 1]
                list[i + 1] = pos


list_1 = [54, 26, 93, 17, 77, 31, 44, 55, 20]
bubbleSort(list_1)
print(list_1)
