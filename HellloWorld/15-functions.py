def square(number):
    return number * number

print(square(3))

def greet_user(first_name='James', last_name='John'):
    print(f'Hi {first_name} {last_name}')
    print('how r u')


# call function after definition
#greet_user('Roby', 'James') #postional arguments
#greet_user()
#keyword arg eg:
greet_user(last_name="John", first_name="Roby")
