"""
Практическое задание по работе в PyCharm - "Переменные".
Цель: научиться правильно называть переменные и взаимодействовать с ними.
"""

homework_amount = 12
homework_time = 1.5
course_name = 'Python'
one_task_time = homework_time / homework_amount

# В задании указано, что пробелы между словами и символами ":" "," можно ставить на свое усмотрение.
print('Курс:', course_name, ', всего задач:', str(homework_amount), ', затрачено часов:', str(homework_time),
      ', среднее время выполнения:', str(one_task_time), 'часа.')

# Используем конкатенацию строк, чтобы вывод текста был идентичен тексту в задании.
# print('Курс: ' + course_name + ', всего задач:' + str(homework_amount) + ', затрачено часов: ' + str(homework_time) +
#       ', среднее время выполнения: ' + str(one_task_time) + ' часа.')
