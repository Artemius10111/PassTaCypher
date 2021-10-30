import random, string
class generator_logic:
    def __init__(self, type_of_symbols, len_of_password, string_of_password=None) -> int:
        self.type_of_symbols = type_of_symbols
        self.len_of_password = len_of_password
        self.string_of_password = string_of_password
    def generate_password(self):
        if self.type_of_symbols == 1:
            self.string_of_password = string.ascii_letters
        elif self.type_of_symbols == 2:
            self.string_of_password = string.digits
        elif self.type_of_symbols == 3:
            self.string_of_password = string.ascii_letters + string.digits
        elif self.type_of_symbols == 4:
            self.string_of_password = string.ascii_letters + string.digits + string.punctuation
        string_result = ''
        while len(string_result) != self.len_of_password:
            string_result = string_result + random.choice(self.string_of_password)
        return string_result


