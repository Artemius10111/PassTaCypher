import string
from random import choice, random, randint
from generator import generator_logic
a = generator_logic(1, 999)
b = generator_logic(1, 20)
c = generator_logic(1, 20)
d = generator_logic(1, 20)

def cipher(string_) -> str:
    password = list(string_)
    symbols = string.ascii_letters + string.digits + string.punctuation

    list_of_cryptographed_password = []
    list_of_indexes_of_password = []
    for i in password:
        list_of_indexes_of_password.append(symbols.index(i)+1)
        number1 = symbols.index(i)+1
        number2 = symbols.index(choice(symbols))+1
        sum_of_numbers = sum([number1, number2])
        while sum_of_numbers > len(symbols):
            sum_of_numbers = sum_of_numbers - len(symbols)
        list_of_cryptographed_password.append(sum_of_numbers)

    final_password_list = [symbols[i-1] for i in list_of_cryptographed_password]
    final_key = list(map(lambda x,y: x-y, list_of_cryptographed_password, list_of_indexes_of_password))
    final_key = list(map(lambda x: choice([bin(x), oct(x), hex(x)]), final_key))
    password_list_str = "".join(final_password_list)
    final_key_list_str = ".".join(map(str, final_key))
    return [password_list_str, final_key_list_str]


def decipher(dict_) -> dict:
    def check_notation(var):
        if var[0] == "-":
            if var[2] == "b":
                return int(var, 2)
            if var[2] == "x":
                return int(var, 16)
            if var[2] == "o":
                return int(var, 8)
        else:
            if var[1] == "b":
                return int(var, 2)
            if var[1] == "x":
                return int(var, 16)
            if var[1] == "o":
                return int(var, 8)
    list_ = dict_.keys()
    value = dict_.values()
    for i in value:
        list_key = i.split(".")

    list_key = list(map(lambda x: check_notation(x), list_key))
    string_of_password = string.ascii_letters + string.digits + string.punctuation
    for i in list_:
        string_of_letters = "".join(i)
    list_of_indexes_of_password = [string_of_password.index(i) for i in string_of_letters]
    list_key = list(map(lambda x: -(x-1), list_key))
    final_list_of_indexes = [x+y for x,y in zip(list_of_indexes_of_password, list_key)]
    final_List_of_letters = [string_of_password[i-1] for i in final_list_of_indexes]
    return "".join(final_List_of_letters)
