def add_everything_up(a, b):
    pass

    try:
        return round((a + b), 3)

    except Exception as exc:
        return f'{a}{b},  ({exc})'


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
