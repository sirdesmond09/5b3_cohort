# my_var = "5"
# print(type(my_var))
# my_int = float(my_var)
# print(type(my_int))

### QUESTION 1
# a = 5
# b = 7
# c= -1

# numerator = -b + (b**2 - 4*a*c)**0.5
# denom = 2*a

# print(numerator/denom)

# ##### QUESTION 2
# pi = 3.142
# r = 5

# volume = (4/3)*pi*(r**3)
# print(volume)

# #### QUESTION 3
# book_price = 24.95
# discount = 0.6
# ship_1 = 3
# ship_2 = 0.75
# num_of_books = 60

# total_book_price = book_price*discount*num_of_books

# total_checkout_price = total_book_price+ship_1+(ship_2*59)

# print(total_checkout_price)


##### QUESTION 4
start_time  = 6*3600 + (52*60)
easy_time = ((8*60) +15)*2
tempo_time = ((7*60) +12)*3

run_time = easy_time + tempo_time

end_time = start_time + run_time
end_time_hr = end_time//3600
end_time_min = (end_time%3600)//60
end_time_sec = (end_time%3600)%60

print(end_time_hr, ":", end_time_min, ":" , end_time_sec, "am")