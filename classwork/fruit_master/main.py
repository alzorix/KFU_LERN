'''Спросить у пользователя строку с фруктами через запятую
 (например: “apple, banana, orange, apple, kiwi”) и превратить её в список.
'''

def register_fruit():
    fruit_list = input("Введите список фруктов через запятую:").split(",")
    return fruit_list

'''Убрать пробелы у каждого фрукта.'''
def delete_space_in_list(fruit_list:list) -> list: 
    list_without_space = list()
    for element in fruit_list:
        line_without_space = ""
        for letter in element:
            if letter != "":
                line_without_space += letter
        list_without_space.append(line_without_space)

    return list_without_space
'''Сделать так, чтобы все фрукты начинались с заглавной буквы (Apple, Banana …).'''

def capitalize_letters_at_the_beginning_of_a_word(fruit_list:list) -> list:
    list_with_capitalize_letters = list()
    for element in fruit_list():
        element_letters_at_the_beginning_of_a_word = element.capitalize()
        list_with_capitalize_letters.append(element_letters_at_the_beginning_of_a_word)
    return list_with_capitalize_letters
#Убрать повторы с помощью множества (set).
def delete_repeats(fruit_list:list) -> list:
    return list(set(fruit_list))
#Вывести список фруктов в алфавитном порядке
def print_in_alphabetical_order(fruit_list:list):
    fruit_list.sort()
    for element in fruit_list:
        print(element)






print(register_fruit())