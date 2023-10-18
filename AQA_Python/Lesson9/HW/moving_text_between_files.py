new_file_name = input('Enter the name of new txt file :')

with open('test.txt', 'r', encoding='utf8') as txt_file:
    with open(f'{new_file_name}.txt', 'a') as new_txt_file:
        for line in txt_file:
            new_txt_file.write(line)
