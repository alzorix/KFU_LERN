'''На вход функция получает список списков с оценками студентов, например [[5, 4, 3], [2, 5], [4]].
Нужно вернуть один список, в котором все оценки будут в один ряд.
Пример:
grades = [[5, 4, 3], [2, 5], [4]]
flatten_grades(grades)  # [5, 4, 3, 2, 5, 4]
'''
def flatten_grades(grades):
    result = []
    for grade in grades:
        result.extend(grade)
    return result

'''Функция: top_two(grades)
Описание:
На вход функция получает кортеж с оценками студента, например (5, 3, 4, 5).
Нужно вернуть кортеж из двух максимальных оценок.
Пример:
grades = (5, 3, 4, 5)
top_two(grades)  # (5, 5)
'''

def top_two(grades:tuple):
    return tuple(sorted(grades,reverse=True)[0:2])
grades = [5, 4, 3, 2, 5, 4]
print(top_two(grades))

'''Подзадание 3. Работа со словарями
Функция: average_score(students)
Описание:
На вход функция получает словарь вида {"Alice": [5, 4, 3], "Bob": [2, 5, 4]}.
Нужно вернуть новый словарь, где каждому студенту соответствует средняя оценка.
Пример:
students = {"Alice": [5, 4, 3], "Bob": [2, 5, 4]}
average_score(students)  # {"Alice": 4.0, "Bob": 3.6666666666666665}
'''

def average_score(students:dict):
    for student in students:
        grades = students[student]


        sr_grade = sum(grades) / len(grades)
        students[student] = sr_grade
    return students


students = {"Alice": [5, 4, 3], "Bob": [2, 5, 4]}
print(average_score(students))

'''Подзадание 4. Работа с множествами
Функция: unique_subjects(*grades_lists)
Описание:
На вход функция получает несколько списков предметов, например ["Math", "Bio"], ["Bio", "PE"].
Нужно вернуть множество всех уникальных предметов.
Пример:
unique_subjects(["Math", "Bio"], ["Bio", "PE"])  # {"Math", "Bio", "PE"}
'''

def unique_subjects(*grades_lists):
    unique = set()
    for someone_list in grades_lists:
        for subject in someone_list:
            unique.add(subject)
    return unique
print(unique_subjects(["Math", "Bio"], ["Bio", "PE"]))

'''Подзадание 5. Побитовые операции
Функция: flag_students(ids)
Описание:
На вход функция получает список числовых ID студентов.
Нужно вернуть число, где каждый ID представлен в виде бита, объединённого побитовым ИЛИ.
Пример:
ids = [1, 2, 4]
flag_students(ids)  # 7
'''
def flag_students(ids):
    res = 0
    for id in ids:
        res = res|id
    return res
ids = [1, 2, 4]
print(flag_students(ids))

'''Подзадание 6. Кодовые таблицы
Функция: encode_names(names)
Описание:
На вход функция получает список имён студентов ["Ann", "Борис"].
Нужно вернуть список списков числовых кодов символов.
Пример:
names = ["Ann", "Борис"]
encode_names(names)  
# [[65, 110, 110], [1041, 1086, 1088, 1080, 1089]]
'''

def encode_names(names):
    res = []
    for name in names:
        name_codes = list()
        for char in name:
            name_codes.append(ord(char))
        res.append(name_codes)
    return res
names = ["Ann", "Борис"]
print(encode_names(names))

