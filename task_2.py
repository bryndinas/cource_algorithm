from uuid import uuid4
import hashlib

def chek_passwd():
    passwd = input('Введите пароль\n')
    salt = 'salt_example'
    try:
        res = hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()
        print(f'В базе данных хранится строка {res}')
    finally:
        passwd = input('Введите пароль еще раз для проверки\n')
        chek = hashlib.sha256(salt.encode() + passwd.encode()).hexdigest()
        if res == chek:
            print('Вы ввели верный пароль')
        else:
            print('Вы ввели неверный пароль')


if __name__ == "__main__":
    chek_passwd()