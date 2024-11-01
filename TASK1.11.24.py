import keyboard
try:
    print('Приветствие в программе Арсланова')
    dictionary = { "яблоко": {"apple", "pome"}, "банан": {"banana"}, "груша": {"pear"}, "апельсин": {"orange"}, "киви": {"kiwi"}, }
    possible_keys = ('ctrl+f', 'esc', 'tab', 'enter')
    print('**Памятка**')
    print('Нажмите "ctrl+f" для поиска слова в словаре')
    print('Нажмите "esc" для поиска слова в словаре')
    print('Нажмите "tab" для поиска слова в словаре')
    print('Нажмите "enter" для поиска слова в словаре')
    print('**Памятка**')
    while True:
        if keyboard.is_pressed('ctrl+f'):
            info = input('Введите слово для проверки в списке:')
            if info in dictionary:
                print(dictionary[info])
            else:
                print('Такого слова нет!')
            break
        if keyboard.is_pressed('esc'):
            print('Работа завершена!')
            break
        if keyboard.is_pressed('+'):
            translation = set()
            input_orig = input('Введите слово на Русском языке:')
            input_translation = input('Введите перевод слова')
            if input_orig in dictionary or input_translation in dictionary:
                print('Такое слово уже есть, введите другое название')
                break
            dictionary[input_orig] = input_translation
            translation.add(input_orig)
            translation.add(input_translation)
            print(f'Слово {input_orig} и перевод {dictionary[input_orig]} добавляем в словарь')
            print('Чтобы добавить дополнительный перевод нажмите: "tab"')

        while True:
            if keyboard.is_pressed('tab'):
                    add_translation = input('Введите дополнительный перевод:')
                    dictionary[input_orig] = input_translation, add_translation
                    print(f'Весь список: {dictionary}')
            if keyboard.is_pressed('shift'):
                break
except ValueError as e:
    print("Некорректный ввод данных!")