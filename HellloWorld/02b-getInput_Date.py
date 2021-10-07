weight = input('Weight: ')
unit = input('(L)bs or (K)g: ')
if(unit.upper()=='L'):
    print (f'{int(weight) * 0.45} Kg')
elif(unit.upper()=='K'):
    print (f'{int(weight) / 0.45} Lbs')

# weight_in_pound = input("Enter Weight (\"in pounds\"): ")
# weight_in_kilo = int(weight_in_pound) * 0.45
# print(weight_in_kilo)


#use 3 quotes to span multiple lines
course = '''
Hi abc,
This is a test email

'''

# birth_year = input('Birth year: ')
# print(type(birth_year))
# age = 2021 -  int(birth_year)
# print(type(age))
# print(age)
