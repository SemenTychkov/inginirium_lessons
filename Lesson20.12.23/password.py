def ask_password():
    password = input('ведите пароль')
    if password == 'пароль':
        print('пароли совпадают')
    else:
        print('пароли не совпадают')


ask_password()