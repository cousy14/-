command = input('Введите через пробелы математическое действие и два целых числа')
command_list = command.split()
c = command_list[0]
a = int(command_list[1])
b = int(command_list[2])
# print(c)
# print(a)
# print(b)
# # c = input('Введите математическое действие')
# # a = int(input('1-ое значение'))
# # b = int(input('2-ое значение'))

print('Результат математического действия', c, a, b)

assert c in {"+", "-", "/", "*"}


if a >= 0 and  b >= 0:
    if c == '+':
        result = a + b
        print(result)
    elif c == '-':
        result = a - b
        print(result)
    elif c == '*':
        result = a * b
        print(result)
    elif c == '/':
      if b == 0:
        try:
          result = (a / b)
        except ZeroDivisionError:
	        print('Делить на 0 нельзя')
      else:
        result = round((a / b), 2)
        print(result)
        
    else:
        print('Проверьте корректность ввода математического действия')
else:
    print('Вы ввели неверный номер')
