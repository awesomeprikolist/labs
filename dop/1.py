synonyms = {}

with open('synonyms.txt', 'r', encoding='utf-8') as file:
    for line in file:
        try:
            word, synonyms_str = line.strip().split(' - ')
            synonyms[word.lower()] = {synonym.lower(): True for synonym in synonyms_str.split('; ')}
        except ValueError:
            pass

while True:
    user_input = input('Введите слово: ').lower()
    if user_input in synonyms:
        print(', '.join(synonyms[user_input]))
        is_suitable = input('Подходят ли Вам предложенные варианты? (да/нет): ').lower()

        if is_suitable == 'нет':
            new_synonym = input('Введите новый синоним: ')
            synonyms[user_input].update({new_synonym.lower(): True})
            with open('synonyms.txt', 'a', encoding='utf-8') as f:
                f.write(f"{user_input} - {new_synonym}\n")
                print(f"Синоним добавлен в базу.")

    elif any(user_input in synonyms[word] for word in synonyms):
        result = "".join(next(word for word in synonyms if user_input in synonyms[word]))
        print(result)

    else:
        print(f"Слово '{user_input}' не найдено в базе данных.")

    is_repeat = input('Хотите продолжить? (да/нет): ').lower()
    if is_repeat == 'нет':
        break

with open('synonyms.txt', 'w', encoding='utf-8') as f:
    for word, syn_set in synonyms.items():
        syn_list = list(syn_set)
        f.write(f"{word} - {'; '.join(syn_list)}\n")
        