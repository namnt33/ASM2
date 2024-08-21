if __name__ == '__main__' :
    num1 = int(input('Enter num 1:'))
    num2 = int(input('Enter num 2:'))
    num3 = int(input('Enter num 3: '))

    if num3 > num2 > num1 :
        print('num3 is max and num1 is min')
    elif num3 < num2 < num1 :
        print('num3 is min and num1 is max')
    elif num2 > num3 > num1 :
        print('num2 is max and num1 is min')
    else : print('num2 is min and num1 is max')
