stats = {'facebook': 55, 'yandex': 120, 'vk': 115, 'google': 99, 'email': 42, 'ok': 98}
max_num = 0
max_name = None
for name, num in stats.items():
    if max_num < num:
        max_num = num
        max_name = name
print(f'{max_name} - канал с максимальным объемом {max_num} чего-то там')
