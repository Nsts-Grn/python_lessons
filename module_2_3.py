my_list = [42, 69, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]
neutral = 0 
while len(my_list) > 0:
    numbers = my_list[neutral]
    neutral = neutral + 1
    if numbers == 0:
        continue
    elif numbers < 0:
        break
    else:
        print(numbers)


