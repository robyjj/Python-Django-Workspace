numbers = [5, 2, 1, 9, 8, 9]
uniques = []
for number in numbers:
    if number not in uniques:
       uniques.append(number)

print(uniques)


# numbers = [5, 2, 1, 9, 8, 9]
# numbers.sort()
# ctr =1
# for i in numbers:
#     if numbers[ctr] == i:
#        numbers.remove(i)
#     ctr += 1
# print(numbers)