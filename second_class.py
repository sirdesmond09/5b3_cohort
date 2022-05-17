new_string = "This is a string."

new_doc_string = """This is a nice sting and I 

can move to the next 


line and work!

    thanks."""
    
    
string1 = "This is a string"
string2 = "I love this string."

# print(string1+ " " +string2)

# print(string1, string2)

# print(string1[-1])


### FORMATING


# name = input("Enter your name: ")

# print(f"""Welcome , {name}.

# You have signed up successfully.

# Cheers,
# Newlife Team.""")


# first_name = input("First name: ")
# last_name = input("Last name: ")

# username = last_name[:3]+first_name[-2:]

# print(f"""Welcome, {first_name}.
# Your account has been created and your username is {username}.

# Kindly proceed to your portal to login.

# Cheers,
# Freshest Universe.""")


# print("The man said, \"You do what you have to do, so you can do what you want to do.\" I hope you were inspired. ")

# print('The man said, "You do what you have to do, so you can do what you want to do." I hope you were inspired.')

# print("This is the boy's dog.\nHis name is Jack!")

### STRING METHODS


# name = input("Enter your name:\n::>>")

# a = name.split()
# print(a)
# print(a[1][2:5])

# a = ["david", "adeleke"]

# print(" ".join(a).title())


text = """An alternative is designed development, in which high-level insight into the problem can
make the programming much easier. In this case, the insight is that a Time object is really
a three-digit number in base 60"""


search_for = input(">").lower()
print(f"{text.lower().count(search_for)} result(S) found")
print(text.lower().replace(search_for, search_for.upper()))

import csv
from tabulate import tabulate
csv.reader()

