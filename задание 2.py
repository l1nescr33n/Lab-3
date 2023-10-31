def find_common_participants(participants, second_participants, separator=","):
    participants = participants.split(separator)
    # Разделение списка участников первой группы на список строковых переменных с фамилиями
    second_participants = second_participants.split(separator)
    # Разделение списка участников второй группы на список строковых переменных с фамилиями
    participants = sorted(list(set(second_participants).intersection(participants)))
    # Нахождение соответствий в двух списках, создание отсортированного списка
    print(participants)  # Вывод результатов работы функции на экран
    return participants  # Возвращение аргумента функции


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

find_common_participants(participants_first_group, participants_second_group, separator="|")
# Вызов функции и изменение для данного случая параметра по умолчанию
