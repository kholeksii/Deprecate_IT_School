params = {'v': 'some_id', 'list': 'some_list', 'index': '6', 't': '0s'}
initial_str = 'https://www.youtube.com/watch?'
expected_link = 'https://www.youtube.com/watch?v=some_id&list=some_list&index=6&t=0s'

for key, value in params.items():
    initial_str = initial_str+key+'='+value+'&'

initial_str = initial_str[:-1]

print(initial_str)
print(f'The links are the same: {expected_link == initial_str}')
