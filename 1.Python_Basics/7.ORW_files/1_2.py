from pprint import pprint


def get_recipes(recipes_file='./recipes.txt'):
    with open(recipes_file, encoding='utf-8') as file:
        cook_book = {}
        for dish in file:
            dish_name = dish.strip()
            counter = int(file.readline().strip())
            temp_data = []
            for item in range(counter):
                ingredient, quantity, measure = file.readline().split('|')
                temp_data.append({'ingredient_name': ingredient, 'quantity': quantity, 'measure': measure})
            cook_book[dish_name] = temp_data
            file.readline()
        return cook_book


def get_shop_list_by_dishes(dishes, persons):
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book[dish]:
            new_shop_list_item = dict(ingredient)
            new_shop_list_item['quantity'] = int(persons) * int(new_shop_list_item['quantity'])
            if new_shop_list_item['ingredient_name'] not in shop_list:
                shop_list[new_shop_list_item['ingredient_name']] = new_shop_list_item
            else:
                shop_list[new_shop_list_item['ingredient_name']]['quantity'] += new_shop_list_item['quantity']
    return shop_list


def print_shop_list(shop_list):
    for shop_list_item in shop_list.values():
        pprint(
            '{} {} {}'.format(shop_list_item['ingredient_name'], shop_list_item['quantity'], shop_list_item['measure']))


print('Задание_1')
cook_book = get_recipes()
pprint(cook_book)
print('Задание_2')
shop_list = get_shop_list_by_dishes(['Запеченный картофель', 'Омлет'], 2)
print_shop_list(shop_list)
