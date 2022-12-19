import os

list_of_all_files = os.listdir()
txt_files = filter(lambda x: x.endswith('.txt'), list_of_all_files)

dict_files = {}

for files in txt_files:
    with open(files, encoding='utf-8') as f:
        count = 0
        for lines in f:
            count += 1
        dict_files.setdefault(files, []).append(count)

sorted_dict = {}

sorted_keys = sorted(dict_files, key=dict_files.get)
for w in sorted_keys:
    sorted_dict[w] = dict_files[w]

with open('result/result.txt', 'w', encoding='utf-8') as outfile:
    for file_name in sorted_dict:
        with open(file_name, encoding='utf-8') as infile:
            outfile.write(file_name + '\n')
            outfile.write(str(sorted_dict.get(file_name)) + '\n')
            outfile.write(infile.read() + '\n')