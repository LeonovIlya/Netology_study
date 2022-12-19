ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

# 1
print(list(set(ids['user1']) | set(ids['user2']) | set(ids['user3'])))

# 2
my_list = []
for _, id in ids.items():
    for num in id:
        my_list.append(num)
print(set(my_list))
