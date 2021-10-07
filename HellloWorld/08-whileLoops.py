chances = 3
answer = 7

while chances > 0:
    number = input('Guess: ')
    chances -= 1
    if int(number) == answer:
        print ('You won')
        break
else:
    print ('You lose')



# i=1
# while i<=5:
#     print('*' * i)
#     i += 1