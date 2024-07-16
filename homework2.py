"""
Практическое задание по работе в PyCharm - "Переменные".
Цель: научиться правильно называть переменные и взаимодействовать с ними.
"""

homework_amount = 12
homework_time = 1.5
course_name = 'Python'
one_task_time = homework_time / homework_amount

print('Курс: ' + course_name + ', всего задач:' + str(homework_amount) + ', затрачено часов: ' + str(homework_time) +
      ', среднее время выполнения: ' + str(one_task_time) + ' часа.')
# Между "всего задач:" и "12" пробел намеренно пропущен, т.к. в задании указано именно так.
