# Nationality must start with capital letter 

country = input ('What is your nationality: ')
age = input ('What is your age: ')
age = int (age)
if country == 'Taiwan':
	if age >= 18:
		print('you can take the drivers license test')
	else:
		print('you are not yet able to take your drivers license test')
elif country == 'USA':
	if age >= 16:
		print('you can take the drivers license test')
	else:
		print('you are not yet able to take your drivers license test')
		