en_ru_dict = {}
ru_en_dict = {}
with open("en-ru.txt", "r") as file:
    for line in file:
        if " - " in line: 
            en_word, ru_words = line.strip().split(" - ")
            en_ru_dict[en_word] = ru_words
            ru_words_list = ru_words.split(", ")
            for ru_word in ru_words_list:
                if ru_word in ru_en_dict:
                    ru_en_dict[ru_word] += ", " + en_word
                else:
                    ru_en_dict[ru_word] = en_word


sorted_ru_en = sorted(ru_en_dict.items(), key=lambda x: x[0])

with open("ru-en.txt", "w") as file:
    for ru_word, en_words in sorted_ru_en:
        file.write(f"{ru_word} - {en_words}\n") 
