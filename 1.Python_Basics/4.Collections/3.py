queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт'
    ]

base = {}
for query in queries:
    words = query.split()
    if len(words) in base.keys():
        base[len(words)] += 1
    else:
        base.update({len(words): 1})
for key, value in base.items():
    result = round((value / len(queries)) * 100, 2)
    print(f'Запросов из {key} слов(а): {result}%')
    