# def f(x):
# #     if x>10:
# #        return True
# #     else:
# #         return False
# #
# #
# #
# # a = [14, 0, 5, 79, 645, 93, 7952, 18, 0, 192]
# # b = list(filter(f,a))
# # print(b)

def f(x):
   return x>10




a = [14, 0, 5, 79, 645, 93, 7952, 18, 0, 192]
b = list(filter(f,a))
print(b)


def f(x):
   return x>9 and x<100




a = [14, 0, 5, 79, 645, 93, 7952, 18, 0, 192]
b = list(filter(f,a))
print(b)


# def f(x):
#    return x>9 and x<100
#
#
#
#
# a = [14, 0, 5, 79, 645, 93, 7952, 18, 0, 192]
# b = [i for i in a if i>9 and i<100]
# print(b)

# def f(x):
#    return x>9 and x<100
#
#
#
#
# a = [14, 0, 5, 79, 645, 93, 7952, 18, 0, 192]
# b = [i for i in a if i>9 and i%10==2]
# print(b)


def f(x):
   return x>9 and x<100




a = [14, 0, 5,'', 79, 'hello', [5], ' ',[], 93, 7952, 18, 0, 192]
b = list(filter(bool, a))
print(b)


def f(x):
   return x>9 and x<100




a = [14, 0, 5,'', 79, 'hello', [5], ' ',[], 93, 7952, 18, 0, 192]
b = list(filter(None, a))
print(b)






a = ['world', 'hello','3243', 'potato', 'carrot','hi']
b = list(filter(lambda x:len(x)>5 , a))
print(b)

a = '432fbhsgbHDGHjdfvj345'
b = list(filter(str.isdigit,a))
print(b)


a = '432fbhsgbHDGHjdfvj345'
b = list(filter(str.isalpha,a))
print(b)


a = '432fbhsgbHDGHjdfvj345'
b = list(filter(str.isupper,a))
print(b)

#можно фильтровать словари