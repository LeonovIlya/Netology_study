documents = [
    {"type": "passport", "number": "2207 876234", "name": "Василий Пупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"}
]

directories = {
    '1.Introduction': ['2207 876234', '11-2'],
    '2': ['10006'],
    '3': []
}


def people(documents):
    num_doc_user = input('Введите номер документа: ')
    for doc in documents:
        if doc['number'] == num_doc_user:
            return print(f'Имя владельца документа - {doc["name"].split()[0]}')
    return print('Нет такого документа!')


def shelf(directories):
    num_doc_user = input('Введите номер документа: ')
    for shelf_num, num_doc in directories.items():
        for num_doc1 in num_doc:
            if num_doc_user == num_doc1:
                return print(f'Текущая полка документа - {shelf_num}')
    return print('Нет такого документа!')


def list_docs(documents):
    print('Список всех документов: ')
    for doc in documents:
        print(doc['type'], doc['number'], doc['name'])


def add_doc(documents, directories):
    new_shelf = input('Введите номер полки:')
    if new_shelf not in directories:
        return print('Полки не существует!')
    new_line = dict()
    for key in documents[0]:
        new_line[key] = input(f"Введите данные для поля '{key}': ")
    documents.append(new_line)
    directories[new_shelf].append(new_line['number'])
    return print('Данные добавлены')


def delete(documents, directories):
    num_del = input('Введите номер документа:')
    for record, doc in enumerate(documents):
        if doc['number'] == num_del:
            documents.pop(record)
    for key, value in directories.items():
        if num_del in value:
            value.remove(num_del)
            return print('Данные удалены')
    return print('Документ не найден!')


def move_doc(directories):
    num_doc_user = input('Введите номер документа: ')
    for shelf_num, num_doc in directories.items():
        for num_doc1 in num_doc:
            if num_doc_user == num_doc1:
                new_shelf = input('Введите номер полки, куда переместить: ')
                if new_shelf not in directories:
                    return print('Полки не существует!')
                for key, value in directories.items():
                    if num_doc_user in value:
                        directories[new_shelf].append(num_doc_user)
                        value.remove(num_doc_user)
                        return print('Документ перенесён')
    return print('Нет такого документа!')


def add_shelf(directories):
    add_new_shelf = input('Введите номер новой полки: ')
    if add_new_shelf not in directories:
        directories[add_new_shelf] = list()
        return print('Добавление успешно')
    return print('Такая полка уже существует!')


def main(documents, directories):
    while True:
        user_input = input('Выберите команду:')
        if user_input == 'p':
            people(documents)
        elif user_input == 's':
            shelf(directories)
        elif user_input == 'l':
            list_docs(documents)
        elif user_input == 'a':
            add_doc(documents, directories)
        elif user_input == 'd':
            delete(documents, directories)
        elif user_input == 'm':
            move_doc(directories)
        elif user_input == 'as':
            add_shelf(directories)
        elif user_input == 'quit':
            print('До свидания!')
            break


main(documents, directories)
