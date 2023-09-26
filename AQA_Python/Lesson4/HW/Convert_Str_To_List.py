lst_1 = ['Hillel', 'AQA', 'TEST']
print(f'The Original List :{lst_1}')
stringContainsList = str(', '.join(lst_1))
print(f'The String from the List : {stringContainsList}')
restoredList = stringContainsList.split(', ')
print(f'The Restored List : {restoredList}')