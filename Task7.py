"""Розробіть функцію sanitize_file(source, output), що переписує у текстовий файл output вміст
текстового файлу source, очищений від цифр.

Вимоги:

прочитайте вміст файлу source, використовуючи менеджер контексту with та режим "r".
запишіть новий очищений від цифр вміст файлу output, використовуючи менеджер контексту with та режим "w"
запис нового вмісту файлу output має бути одноразовий і використовувати метод write"""


def sanitize_file(source, output):
    with open(source, 'r') as source_file:
        new_source = source_file.read()
        cleaned_new_source = ''.join([char for char in new_source if not char.isdigit()])

    with open(output, 'w') as output_file:
        output_file.write(cleaned_new_source)