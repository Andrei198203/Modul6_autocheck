# s = "Привет!"
#
# utf8 = s.encode()
# print(utf8)

"""Є два рядки у різних кодуваннях - "utf-8" та "utf-16". Нам необхідно зрозуміти, чи дорівнюються рядки між собою.

Реалізуйте функцію is_equal_string(utf8_string, utf16_string), яка повертає True, якщо рядки дорівнюють
собі, і False — якщо ні."""


def is_equal_string(utf8_string, utf16_string):
    s_from_utf8 = utf8_string.decode('utf-8')
    s_from_utf16 = utf16_string.decode('utf-16')

    if s_from_utf8 == s_from_utf16:
        return True
    else:
        return False