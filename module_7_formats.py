# Использование %:
team1_num = 5
print('В команде Мастера кода участников: %s!' % team1_num)

team2_num = 6
print('Итого сегодня в командах участников: %s и %s!' % (team1_num, team2_num))

print(' ***')

# Использование format():
score_2 = 42
print('Команда Волшебники данных решила задач: {}!'.format(score_2))  # Позиционный параметр.
print('Команда Волшебники данных решила задач: {score_2}!'.format(score_2 = 42))  # Именованный параметр - лучше
                                                                                  # подходит для импорта.

team1_time = 18015.2
print('Волшебники данных решили задачи за {} с!'.format(team1_time))  # Позиционный параметр.
print('Волшебники данных решили задачи за {team1_time} с!'.format(team1_time = 18015.2))  # Именованный параметр - лучше
                                                                                          # подходит для импорта.

print(' ***')

# Использование f-строк:
score_1 = 40
score_2 = 42
print(f'Команды решили {score_1} и {score_2} задач.')

# Пример использования функций в f-строках.
def challenge_result(score_1, score_2, team1_time, team2_time):
    if score_1 > score_2 or score_1 == score_2 and team1_time > team2_time:
        result = 'Победа команды Мастера кода!'
    elif score_1 < score_2 or score_1 == score_2 and team1_time < team2_time:
        result = 'Победа команды Волшебники Данных!'
    else:
        result = 'Ничья!'

print(f'Результат битвы: {challenge_result(40, 
										   42, 
										   1552.512, 
										   2153.31451)} команды Мастера кода!')

tasks_total = 82
time_avg = 45.2
print(f'Сегодня было решено {tasks_total} задач, в среднем по {time_avg} секунды на задачу!')

# В качестве дополнения рассчитаем общее время на решение всех задач.
print(f'На решение всех задач ушло {tasks_total * time_avg}')  # Выполним арифметическую операцию внутри f-строки.
