import csv


def open_and_read(filename):
    with open(filename, encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list
