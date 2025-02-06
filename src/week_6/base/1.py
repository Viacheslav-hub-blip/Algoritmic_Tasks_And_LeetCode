import re


class Field(dict):
    def __init__(self):
        super().__init__()
        self.table  = dict()
    @staticmethod
    def convert_tuple(key):
        if type(key) == tuple:
            key = str(key[1]) + str(key[0])
            key.lower()
        print('converted key', key)
        return key

    @staticmethod
    def check_valid_key(key):
        pattern = re.compile(r'[a-zA-Z]{1}\d+|\d+[a-zA-Z]{1}')
        if not isinstance(key, (tuple, str)):
            raise TypeError('key must be a tuple')

        if re.fullmatch(pattern, key):
            return True
        else:
            raise ValueError

    def __setitem__(self, key, value):
        key  = Field.convert_tuple(key)
        if Field.check_valid_key(key):
            super(Field, self).__setitem__(key, value)

    def __getitem__(self, key):
        key = Field.convert_tuple(key)
        if Field.check_valid_key(key):
            if super(Field, self).__getitem__(key):
                return super(Field, self).__getitem__(key)
            else:
                return None

    def __delitem__(self, key):
        key = Field.convert_tuple(key)
        if Field.check_valid_key(key):
            super(Field, self).__delitem__(key)

    def __missing__(self, key):
        return ""

    def __contains__(self, key):
        key = Field.convert_tuple(key)
        if Field.check_valid_key(key):
            return self[key] != self.__missing__(1)

field = Field()
field.__setitem__((1, 'A'), 10)
field.__setitem__((2, 'A'), 15)
print(field.__getitem__('2A'))
print(field.__getitem__('A2'))
print('1A' in field)
print((1, 'a') in field)

