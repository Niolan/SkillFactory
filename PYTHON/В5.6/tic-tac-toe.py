# My first programm
# It's cool!
def show_field(field):
	print(f'  0 1 2')
	for i in range(len(field)):
		print(i, *field[i])

def asking_user(field, user):
	while True:
		text_coord = input(f'Введите координаты Вашего хода ({user}), числом от 0 до 2, через пробел:')
		if len(text_coord.split()) != 2:
			print('Вы ввели только одну координату')
			continue
		row, col = text_coord.split()
		if not row.isdigit() or not col.isdigit():
			print('Вы использовали недопустимый текстовый формат')
			continue
		x, y = int(row), int(col)
		if not all ([0 <= x <= 2, 0 <= y <= 2]):
			print('Вы указали координаты за пределами поля')
			continue
		if field[x][y] != '-':
			print('Данная ячейка занята!')
			continue
		return x, y
			
def whoose_step(step):
	
	return ('x' if step % 2 else 'o')

def tr_matrix(field):
	transpond_field = []
	for i in range(len(field[0])):
		result = []
		for j in field:
			result.append(j[i])
		transpond_field.append(result)
	return transpond_field

def dioganals(field):
	first = [field[0][0]] + [field[1][1]] + [field[2][2]]
	second = [field[2][0]] + [field[1][1]] + [field[0][2]]
	return ([first] + [second])

def is_win(field, user):
	win_combination = [user, user, user]
	return win_combination in (field + tr_matrix(field) + dioganals(field))

def entrance_game(field):
	step = 1
	while step <= 9:
		show_field(field)
		user = whoose_step(step)
		x, y = asking_user(field, user)
		field[x][y] = user

		if is_win(field, user):
			show_field(field)
			print(f'Играок, играющий за {user} выиграл!')
			break
		else:
			step += 1
	else:
		show_field(field)
		print('Ничья!')

field = [['-']*3 for _ in range(3)]
entrance_game(field)