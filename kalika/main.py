#калікулятор v1

what = input(' виберіть операцію (+, -, *, /, **): ')
a = float(input(' ведіть перше число: '))
b = float(input('ведіть друге число: '))

if what == '+':
    c = a * b
    print('result: ' + str(c))
elif what == '-':
    c = a - b
    print('result: ' + str(c))
elif what == '*':
    c = a * b
    print('result: ' + str(c))
elif what == '/':
    c = a / b
    print('result: ' + str(c))
elif what == '**':
    c = a ** b
    print('result: ' + str(c))
else:print(' дибіл сказано +, -, *, /, **')