from file_action.openfile import open_and_read
from file_action.writenewfile import write_new_file

if __name__ == '__main__':
    open_and_read('phonebook_raw.csv')
    write_new_file('phonebook_new.csv')

