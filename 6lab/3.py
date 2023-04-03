students = {
    "Иванов": {"английский", "испанский", "французский"},
    "Петров": {"английский", "немецкий", "китайский", "японский"},
    "Сидоров": {"английский", "немецкий", "французский"},
    "Кузнецов": {"английский", "китайский"},
    "Смирнов": {"испанский", "французский", "китайский"},
    "Козлов": {"английский", "китайский", "японский", "корейский", "французский"}
}


all_languages = set()
for languages in students.values():
    all_languages.update(languages)
    
print("Количество различных языков, которые знают студенты:", len(all_languages))
print("Отсортированный список языков, которые знают студенты:", sorted(all_languages))

chinese_speakers = []
for student, languages in students.items():
    if "китайский" in languages:
        chinese_speakers.append(student)

print("Список студентов, которые знают китайский язык:", chinese_speakers) 