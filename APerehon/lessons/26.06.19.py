# import msvcrt
#
# i = 0
# while True:
#     if msvcrt.kbhit():
#         key = msvcrt.getch().decode()
#         if key == "j":
#             a = input("-->")
#             print(i)
#     i += 1

def f(a:int,c:int)->str:
    return str(a)+str(c)

# a = f(4,5)
# # print(a)