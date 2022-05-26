# a = {1,2,3,4}
# b = {4,5,2,3,4}

# a.syme

# eng = input("Enter the total number of the students\n::>")
# eng_set = set(input("Enter the roll numbers of the english student subscribers\n::>").split())


# frn = input("Enter the total number of the students\n::>")
# frn_set = set(input("Enter the roll numbers of the french student subscribers\n::>").split())

# print(len(frn_set.symmetric_difference(eng_set)))


import random


# dict_A = {"A":1, "B":2, "C":3, "D":4}

# # print(dict_A["A"])

# dict_A["B"]=59

# dict_A["new_key"] = "new_value"

# print(dict_A.get("A", "This key does not exist."))

my_arr = [random.choice(range(10)) for i in range(10000000)]
# print(a)


# my_arr = [0, 4, 9, 7, 1, 1, 3, 4, 7, 8, 8, 0, 3, 1, 3, 2, 4, 8, 3, 2, 4, 6, 7, 8, 3, 6, 3, 7, 5, 6, 1, 0, 2, 7, 5, 4, 3, 5, 0, 7, 3, 7, 9, 7, 1, 7, 6, 0, 5, 2] 
a ={}
for ele in set(my_arr):
    a[ele] = my_arr.count(ele)
    
print(a)

print()
 
freq = {}

for ele in my_arr:
    freq[ele] = freq.get(ele,0) + 1

print(freq)


