boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']

if len(boys) == len(girls):
    match = list(zip(sorted(boys), sorted(girls)))
    print('Идеальные пары:')
    for pare in match:
        print(f'{pare[0]} и {pare[1]}')
else:
    print('Кто-то может остаться без пары!')
