def cal (oper,int_1,int_2):
    oper = input('Введите знак операции')
    int_1 = int(input('Введите первое число'))
    int_2 = int(input('Введите второе число'))
    if oper == 0:
        return print('Выход')
    elif oper == '+':
        return print(int_1+int_2)
    elif oper == '-':
        return print(int_1-int_2)
    elif oper == '*':
        return print(int_1*int_2)
    elif oper == '/':
        return print(int_1/int_2)

a = (cal(1,2,3))
print(a)
