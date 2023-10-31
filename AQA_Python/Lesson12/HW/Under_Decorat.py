def func_name(func):
    def wrapper(*args):
        print(f'Function title = {func.__name__}')
        result = func(*args)
        return result
    return wrapper

@func_name
def my_max(*args):
    max_value = args[0]
    for value in args:
        if value > max_value:
            max_value = value
    return max_value

@func_name
def my_min(*args):
    min_value = args[0]
    for value in args:
        if value < min_value:
            min_value = value
    return min_value


print(my_min(1, 6, 2))
print(my_max(1, 6, 2))
