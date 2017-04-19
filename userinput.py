cards=['ace', 'king', 'queen', 'jack', 'ten']

while True:
    user_input = input('Enter your card: ')
    if user_input in cards:
        print('I have your card.')
        break;
    else:
        print('I do not have your card.')