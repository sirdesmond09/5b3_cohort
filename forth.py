# def factorial(n):
#     if n==1:
#         return 1
#     if n == 0:
#         return 1
#     recurse = n * factorial(n-1)
#     print(recurse)
#     return recurse


# factorial(5)


# score = int(input("Enter your exam score:\n:>"))

# if score <= 100:
#     if score >= 90:
#         print('A')
#     elif score >= 80:
#         print("B")
#     elif score >= 70:
#         print("C")
#     elif score >= 60:
#         print("D")
#     elif score >= 50:
#         print("E")
#     elif score >= 40:
#         print("F")
#     else:
#         print("Comrade go learn work.")
# else:
#     print("Even me no do reach that one!")
    
# my_str = "this is a lovely string"
# a = list(map(lambda f:f.upper(), my_str))
# print("".join(a))

# import random

# print("Guess the computer's choice to win the prize.")
# a = [1,2,3,4,5,6,7]
# print("Select a number from", a)
# # random.shuffle(a)
# # b = random.sample(a,3)
# random.shuffle(a)
# com_choice= random.choice(a)
# user = int(input("Your choice\n:>"))
# if user == com_choice:
#     print("You win")
# else:
#     if user > com_choice:
#         print("Too high")
#     else:
#         print("Too low")
#     print("You lose")
    
    
# import random

# options = ["r", "p", "s"]
# print("""Select R for rock, P for paper and S for scissors.""")
# com_choice = random.choice(options)
# player_choice = input(">").lower()
# if player_choice in options:
#     if player_choice == options[0] and com_choice==options[2]:
#         print("You win")
#         print("Computer choose", com_choice)
#     elif player_choice == options[2] and com_choice==options[1]:
#         print("You win")
#         print("Computer choose", com_choice)
#     elif player_choice == options[1] and com_choice==options[0]:
#         print("You win")
#         print("Computer choose", com_choice)
#     elif player_choice==com_choice:
#         print("It's a tie")
#     else:
#         print("You lose")
#         print('Computer choose', com_choice.title())
# else:
#     print("Invalid input")

# for i in range(10):
#     if i == 5:
#         # break
#         continue
#     print(i)
a = 0
for i in range(90, 120):
    if i%2==1:
        a+=1
        print(i)
print(" ")       
print(a)
print(" ")        
        

b = [1,2,3,4,15,22,21,33,50,55,72,66,95]
c = 0
for i in b:
    if i%3==0 or i%5==0:
        print(i)
        c+=1
print(' ')
print(c)