if __name__ == '__main__' :
    fullName = input('Enter your name:')
    age = int(input('Enter your age:'))

    if age >=60:
        print('You are old man')
    elif age >= 30:
        print('You are man')
    elif age >= 20:
        print('You are young man')
    elif age >= 10:
        print('you are teenager')
    else: print('You are kid')