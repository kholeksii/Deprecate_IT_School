result_link = 'https://www.youtube.com/watch?v=some_id&list=some_list&index=6&t=0s'

symbol_amount_dict = {}

for symbol in result_link:
    amount = result_link.count(symbol)
    symbol_amount_dict[symbol] = amount

print(symbol_amount_dict)