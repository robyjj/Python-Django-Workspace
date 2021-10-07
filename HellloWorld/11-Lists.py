#Largest element in list
numbers = [5, 2, 1, 9, 8, 9]
numbers.append(20) #adds at end of list
numbers.insert(0, 14) #adds 14 at beginning of list
numbers.remove(9) #removes first occurence of 9
numbers.pop() #removes last number
print(numbers)

print(numbers.index(5)) #9 , prints index of 5 , which is 1

print (5 in numbers) #True , checks if number is in list
numbers.sort()
print (numbers)
numbers.reverse()
print (numbers)
numbers_copy = numbers.copy()
numbers_copy.append(22)
print (numbers)
print (numbers_copy)


#numbers.clear()
#len = len(numbers)
max = numbers[0]
for num in numbers:
    if num > max:
        max = num
print(f'Maximum number is {max}')


###############################################################
# names = ['john', 'james', 'pinkz', 'leon', 'lilly']
# print(names[0]) #John
# print(names[2:]) #['pinkz', 'leon', 'lilly']
# print(names[2:4]) #['pinkz', 'leon'] will print till "end -1"
# print(names[0]) #John
