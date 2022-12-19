import csv
from main_functions import main
from file_action.openfile import open_and_read


def write_new_file(filename):
    with open(filename, 'w', encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(main(open_and_read('phonebook_raw.csv')))
        return print('Новый файл phonebook_new.csv успешно создан')