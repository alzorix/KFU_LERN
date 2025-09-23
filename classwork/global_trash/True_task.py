'''Денисов
Задача: "Система учёта личных финансов"
Программа помогает вести учёт доходов и расходов.
 Можно добавлять операции(сумма, дата и тип расходов),
  видеть статистику за месяц, и определять самые крупные траты.
   Типы расходов можно хранить в словаре'''
from mimetypes import read_mime_types

history = list() #[Дата;тип операции [0-расход,1 - доход],сумма операции,(тип расхода,если расход)]
type_sendings = dict()
type_sendings[0] = "ЖКХ"
type_sendings[1] = "Интернет"

from datetime import datetime
current_month = datetime.today().month
current_year = datetime.today().year



def add_operation():

	day, month, year = map(int, input("Введите дату в формате: число месяц год в числах через пробел: ").split())
	data = (day, month, year)
	 
	type_operation,summa_operation = input("[тип операции,сумма операции]:").split()
	if type_operation == "0":
		type_sending = input(f"Введите тип траты,вы можете: \n {type_sendings.keys()} \n Поле ввода:")
		history.append(	(data,int(type_operation),int(summa_operation),int(type_sending)) )
	else:
		history.append(	(data,int(type_operation),int(summa_operation),-1) )

	
from copy import deepcopy
def print_history():
	current_history = deepcopy(history)
	current_history.sort()
	for x in current_history:
		data,type_operation,summa_operation,type_sending = x
		if data[1] == current_month:	
			if data[1] == current_month:print(data,type_operation,summa_operation,type_sending)
def give_me_max_trata():
	temp_list = list()
	print("data type_operation summa_operation")
	for operation in history:
		data,type_operation,summa_operation,type_sending = operation
		if type_operation == 0:
			if data[1] == current_month and data[2] == current_year:
				temp_list.append((summa_operation,type_sending,data))
	temp_list.sort(reverse = True)
	for operation in temp_list:
		print(summa_operation,type_sendings[type_sending],data)

while True:
   ansewer = input("Введите номер функции:\n 0-добавить операцию \n 1-видеть статистику за месяц \n 2-определить самые крупные траты")
   match ansewer:
       case "0":
           add_operation()
       case "1":
           print_history()
       case "2":
       		give_me_max_trata()