"""
Домашняя работа по уроку "Способы вызова функции".
Цель: создать функцию send_email, которая принимает 2 обычных аргумента: сообщение и получатель и 1 обязательно
именованный аргумент со значением по умолчанию - отправитель.
Внутри функции реализовать следующую логику:
- проверка на корректность e-mail отправителя и получателя;
- проверка на отправку самому себе;
- проверка на отправителя по умолчанию.
"""


def email_verification(recipient, sender):  # Функция для проверки наличия элементов '.com', '.ru' и '.net' в почтовых
    # адресах отправителя и получателя.
    if '.com' in recipient and '.com' in sender:
        combination = True
    elif '.ru' in recipient and '.ru' in sender:
        combination = True
    elif '.net' in recipient and '.net' in sender:
        combination = True
    elif '.com' in recipient and '.ru' in sender:
        combination = True
    elif '.com' in recipient and '.net' in sender:
        combination = True
    elif '.ru' in recipient and '.com' in sender:
        combination = True
    elif '.ru' in recipient and '.net' in sender:
        combination = True
    elif '.net' in recipient and '.com' in sender:
        combination = True
    elif '.net' in recipient and '.ru' in sender:
        combination = True
    else:
        combination = False
    return combination


def send_email(message, recipient, *, sender="university.help@gmail.com"):  # Функция для комплексной проверки на
    # соответствие электронных адресов установленным требованиям.
    email = email_verification(recipient, sender)  # Результат функции "email_verification(recipient, sender)".
    if sender == recipient:
        print('Нельзя отправить письмо самому себе!')
    elif '@' not in sender or '@' not in recipient or email is False:
        print('Невозможно отправить письмо с адреса', sender, 'на адрес', recipient)
    elif sender == 'university.help@gmail.com':
        print('Письмо успешно отправлено с адреса', sender, 'на адрес', recipient)
    else:
        print('НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса', sender, 'на адрес', recipient)


# Тестируем программу:
send_email('Это сообщение для проверки связи', 'vasyok1337@gmail.com')
send_email('Вы видите это сообщение как лучший студент курса!', 'urban.fan@mail.ru', sender='urban.info@gmail.com')
send_email('Пожалуйста, исправьте задание', 'urban.student@mail.ru', sender='urban.teacher@mail.uk')
send_email('Напоминаю самому себе о вебинаре', 'urban.teacher@mail.ru', sender='urban.teacher@mail.ru')
