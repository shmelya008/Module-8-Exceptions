def personal_sum(args):
    result = 0
    incorrect_data = 0
    for i in args:
        try:
            result += i
        except TypeError:
            incorrect_data += 1
            print(f'Некорректный тип данных для подсчёта суммы - {i}')
    return result, incorrect_data


def calculate_average(args):
    try:
        average = personal_sum(args)[0] / (len(args) - personal_sum(args)[1])
    except ZeroDivisionError:
        return None
    except TypeError:
        return # f'В (args) записан некорректный тип данных'
    return round(average, 3)


print(f'Результат 1: {calculate_average("1, 2, 3")}')  # Строка перебирается, но каждый символ - строковый тип
print(f'Результат 2: {calculate_average([1, "Строка", 3, "Ещё Строка"])}')  # Учитываются только 1 и 3
print(f'Результат 3: {calculate_average(567)}')  # Передана не коллекция
print(f'Результат 4: {calculate_average([42, 15, 36, 13])}')  # Всё должно работать
print(f'Результат 5: {calculate_average([2, "слово_1", 8, 65, "слово_2", -24, 14, 54, "слово_3", -9, -9, 54])}')
print(f'Результат 6: {calculate_average("")}')
