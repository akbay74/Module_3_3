def print_params1(a = 1, b = 'строка', c = True):
    print(a, b, c)

print_params1()
print_params1(3, 'hello', False)
print_params1(b = 25)
print_params1(c = [1, 2, 3])
print()

values_list = [1, True, 'hello']
values_dict = {'a': 1, 'b': 2, 'c': 3}
print_params1(*values_list)
print_params1(**values_dict)
print()a

values_list_2 = [54.32, 'Строка' ]
print_params1(*values_list_2, 42)