def get_param(first:bool=True):
    try:
        if first:
            param = int(input('Введите первое число\n'))
        else:
            param = int(input('Введите второе число\n'))
    except ValueError:
        print('Вы вместо трехзначного числа ввели строку (((. Исправьтесь\n')
        return get_param(first=first)
    return param

def func():
    oper = input('Введите знак операции или 0 для выхода\n')
    if oper in '+-*/':
        try:
            result = eval(
                oper.join([
                    str(get_param(first=True)), str(get_param(first=False))
                ])
            )
            print('Ваш результат {0}'.format(result))
        except ZeroDivisionError:
            print('Нельзя делить на ноль')
        finally:
            return func()
    elif operation == '0':
        return "Завершение программы"
    else:
        print('Вы ошиблись в вводимом знаке операции')
        return func()

if __name__ == "__main__":
    func()