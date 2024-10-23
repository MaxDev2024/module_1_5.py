immutable_var = (1, 4, 'One', False)
print(immutable_var)
# immutable_var[0] = 3 #'Выдаёт ошибку, так как кортеж хранит в себе неизменяемые элементы'
mutable_list = [1, 4, 'One', False]
print(mutable_list)
mutable_list[2] = 'Four'
print(mutable_list)