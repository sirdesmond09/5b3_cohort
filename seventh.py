# a = [1,2,4,7,[5,9,[8,7],4],3,7]

# b = a[4][1] + a[4][2][0]
# print(b)
# import random
# a = [i for i in range(10)]

# random.shuffle(a)
# print(a.extend())

# # print(sorted(a, reverse=True))

# a.reverse()
# print()

# list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]

# # res = list(filter(None, list1))
# # print(res)
# j=[x for x in list1 if x]
# print(j)


# import random 
# import string

# def generate_otp(n):
#     """Generates n*2 length of otp"""
    
#     otp = []
#     for _ in range(n):
#         otp.append(str(random.choice(range(10))))
#         otp.append(random.choice(string.ascii_letters))
#     random.shuffle(otp)
#     return "".join(otp)

# print(generate_otp(8))


# if -3:
#     print(True)
    
# for num in range(-2,-5,-1):
#     print(num, end=", ")
    
    
# var = 10
# for i in range(10):
#     for j in range(2, 10, 1):
#         if var % 2 == 0:
#             continue
#             var += 1
#     var+=1
# else:
#     var+=1
# print(var)


# for num in range(10, 14):
#     for i in range(2, num):
#        if num%i == 1:
#           print(num)
#           break

x = 0
for i in range(10):
  for j in range(-1, -10, -1):
    x += 1
    print(x)