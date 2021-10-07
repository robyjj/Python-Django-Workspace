command = ''
car_started = False
while True:
    command = input('>').lower()
    if command == 'help':
        print('''
start - to start the car
stop - to stop the car
quit - to exit
        ''')
    elif command == 'start':
        if not car_started:
            print('Car Started..')
            car_started = True
        else:
            print('Car already started')
    elif command == 'stop':
        if car_started:
            print('Car Stopped..')
            car_started = False
        else:
            print('Car already stopped')
    elif command == 'quit':
        break
    else:
        print ('I don\'t understand that..')


