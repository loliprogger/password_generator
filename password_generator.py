import random


def generation(chars_string, password_length, service_name):
    
    final = ''
    final += f'{service_name}   '

    for i in range(password_length):
        final += random.choice(chars_string)
    
    password_txt = open("/Users/internet/Документы/python/password_generator/password.txt", "a+")
    password_txt.write('\n')
    password_txt.write(final, )
    password_txt.close()

    return "Your passwor in 'passwords.txt'"


chars = '+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyz1234567890'
password_length = int(input('Input symbols count: '))
service_name = input('Input service name: ')
print(generation(chars, password_length, service_name))


