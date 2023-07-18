num = float(input())

if num == 0:
    print('zero')
elif num > 0:
    if 1000000 < num:
        print('large positive')
    elif 1 > abs(num) != 0:
        print('small positive')
    else:
        print('positive')
elif 0 > num:
    if 1 > abs(num) != 0:
        print('small negative')
    elif 1000000 < abs(num):
        print('large negative')
    else:
        print('negative')
