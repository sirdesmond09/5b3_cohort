# data = {"name":"wale",
#         "city":"silicon valley",
#         "salary":"$20000",
#         "id":"49729"}

# data["employee_id"] = data.pop("id")

 


# print(data)


# import random

# data = {}

# print("Guess the computer's choice to win the prize.")
# a = [1,2,3,4,5,6,7]


# while True:
#     username = input("Username:\n:>>")
#     trial = 3
#     score = 0
    

#     while trial >0:
#         random.shuffle(a)
#         print("\nSelect a number from", a)
#         com_choice= random.choice(a)
#         user = int(input("Your choice\n:>"))
#         if user == com_choice:
#             print("You win")
#             score+=2
#             trial+=1
#             print(f"You have won an extra trial")
#             print(f"{trial} trial(s) left")
            
#         else:
#             if user > com_choice:
#                 print("Too high")
#             else:
#                 print("Too low")
#             trial-=1
#             print(f"{trial} trial(s) left")
            
#     prev_score = data.get(username, 0)
#     if score > prev_score:
#         print("You just beat your previous high score!🎉🎉")
#         data[username]=score

#     print(f"\nYou scored {score} points")       
#     print("Game over ):")
    
#     choice = input("Play again?Y/n:\n>").lower()
#     if choice == "n":
#         break        


# print(data)

