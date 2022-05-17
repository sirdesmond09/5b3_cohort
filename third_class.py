########### ASSIGNMENT CORRECTION #########

# f_n = int(input("first number:>"))
# s_n = int(input("second number:>"))
# t_n = int(input("third number:>"))

# average = (f_n + s_n + t_n)/3

# print(average)



# user_sentence= (input("enter any choice of your sentence")).lower() 
# user_sentence_split = user_sentence.split(" ", 1)
# first_word= user_sentence_split[0].upper()
# new_user_sentence= first_word+" "+user_sentence_split[1]
# print(new_user_sentence)

# print('Question 2 solution')
# print('Enter a sentence below')
# answer = input(':>').split()
# answer[0] = answer[0].upper()
# # a = answer.split()
# print(f'Solution:\n{" ".join(answer)}')

# study = "I am learning python"
# print(study.replace("I am", "You are"))


###### FUNCTIONS

# def test_function():
#     print(4*2 +2)
    
# test_function()
# result = 4

def fun2(n:int):
    global result
    result = n**2
    return result
    # print("I just ran")


print(fun2(4))

print(result)

# def fun3(a,b,c):
#     print(a,b,c)
    
    
# fun3(1,2,3)
# fun3(a=3,b=1,c=3)

# fun3(2, b=3, c=1)

def mean(arr):
    mean_value =sum(arr)/len(arr)
    return round(mean_value, 2)


print("Calculate your mean")
print("Enter your number seperated by comma")
vals = input(":>").split(',')
# print(vals)
mapped = list(map(int,vals))

print(mean(mapped))
# print(list(mapped))



# print(mean([2,34,54,2,1,4]))


