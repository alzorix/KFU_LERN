import csv
from localization import MESSAGES

students = {}


def add_student():
    """Добавить нового студента."""
    try:
        name = input(MESSAGES["input_name"]).strip()
        if name == "": #Если в поле ничего не ввели
            print(MESSAGES["student_not_found"])
            return

        if name in students: #Студент уже существут
            print(MESSAGES["student_exists"])
            return

        age = int(input(MESSAGES["input_age"]))
        if age <= 0:
            print(MESSAGES["error_age_value"])
            return

        grades_input = input(MESSAGES["input_grades"])
        grades = [int(x) for x in grades_input.split() if x.isdigit()]
        students[name] = {"age": age, "grades": grades}
        print(MESSAGES["student_added"].format(name=name))

    except ValueError:
        print(MESSAGES["error_input"])
    except Exception as error:
        print(MESSAGES["unexpected_error"].format(error=error))


def show_students():
    """Показать всех студентов."""
    if not students:
        print(MESSAGES["no_students"])
        return

    for name, data in students.items():
        grades_str = ", ".join(map(str, data["grades"])) if data["grades"] else MESSAGES["no_grades"]
        print(f"{name} | Возраст: {data['age']} | Оценки: {grades_str}")


def find_student():
    """Найти студента по имени."""
    name = input(MESSAGES["input_search_name"]).strip()
    for student_name, data in students.items():
        if student_name.lower() == name.lower():
            grades_str = ", ".join(map(str, data["grades"])) if data["grades"] else MESSAGES["no_grades"]
            print(f"{student_name} | Возраст: {data['age']} | Оценки: {grades_str}")
            break
    else:
        print(MESSAGES["student_not_found"])


def delete_student():
    """Удалить студента по имени."""
    name = input(MESSAGES["input_delete_name"]).strip()
    if name in students:
        del students[name]
        print(MESSAGES["student_deleted"].format(name=name))
    else:
        print(MESSAGES["student_not_found"])


def add_grade():
    """Добавить новую оценку студенту."""
    name = input(MESSAGES["input_name"]).strip()
    if name not in students:
        print(MESSAGES["student_not_found"])
        return
    try:
        grade = int(input(MESSAGES["input_grade"]))
        if grade < 1 or grade > 5:
            print(MESSAGES["error_grade_value"])
            return
        students[name]["grades"].append(grade)
        print(f"Оценка {grade} добавлена студенту {name}.")
    except ValueError:
        print(MESSAGES["error_not_number"])


def show_students_by_age():
    """Вывести список студентов старше определенного возраста."""
    try:
        age_limit = int(input(MESSAGES["input_age_limit"]))
        found = False
        for name, data in students.items():
            if data["age"] > age_limit:
                grades_str = ", ".join(map(str, data["grades"])) if data["grades"] else MESSAGES["no_grades"]
                print(f"{name} | Возраст: {data['age']} | Оценки: {grades_str}")
                found = True
        if not found:
            print(MESSAGES["no_students_by_age"])
    except ValueError:
        print(MESSAGES["error_not_number"])


def show_students_by_grade():
    """Показать студентов с оценкой выше определенного порога."""
    try:
        grade_limit = int(input(MESSAGES["input_grade_limit"]))
        found = False
        for name, data in students.items():
            if any(g > grade_limit for g in data["grades"]):
                grades_str = ", ".join(map(str, data["grades"])) if data["grades"] else MESSAGES["no_grades"]
                print(f"{name} | Возраст: {data['age']} | Оценки: {grades_str}")
                found = True
        if not found:
            print(MESSAGES["no_students_by_grade"])
    except ValueError:
        print(MESSAGES["error_not_number"])


def export_to_csv():
    """Экспорт студентов в CSV-файл."""
    filename = input(MESSAGES["input_export_filename"]).strip()
    try:
        with open(filename, mode="w", newline="", encoding="utf-8") as file:
            writer = csv.writer(file, delimiter=";")
            writer.writerow(["Имя", "Возраст", "Оценки"])
            for name, data in students.items():
                writer.writerow([name, data["age"], " ".join(map(str, data["grades"]))])
    except Exception as error:
        print(MESSAGES["export_error"].format(error=error))
    else:
        print(MESSAGES["export_success"].format(filename=filename))
    finally:
        print(MESSAGES["export_done"])


def import_from_csv():
    """Импорт студентов из CSV-файла."""
    filename = input(MESSAGES["input_import_filename"]).strip()
    try:
        with open(filename, mode="r", encoding="utf-8") as file:
            reader = csv.DictReader(file, delimiter=";")
            for row in reader:
                name = row["Имя"].strip()
                age = int(row["Возраст"])
                grades = [int(x) for x in row["Оценки"].split()] if row["Оценки"].strip() else []
                students[name] = {"age": age, "grades": grades}
    except FileNotFoundError:
        print(MESSAGES["import_file_not_found"])
    except Exception as error:
        print(MESSAGES["import_error"].format(error=error))
    else:
        print(MESSAGES["import_success"].format(filename=filename))
    finally:
        print(MESSAGES["import_done"])


def main():
    """Главное меню программы."""
    actions = {
        "1": add_student,
        "2": show_students,
        "3": find_student,
        "4": delete_student,
        "5": add_grade,
        "6": show_students_by_age,
        "7": show_students_by_grade,
        "8": export_to_csv,
        "9": import_from_csv,
    }

    while True:
        print(MESSAGES["menu"])
        choice = input(MESSAGES["enter_choice"]).strip()
        if choice == "0":
            print(MESSAGES["exit"])
            break
        action = actions.get(choice)
        if action:
            action()
        else:
            print(MESSAGES["invalid_choice"])


if __name__ == "__main__":
    main()
