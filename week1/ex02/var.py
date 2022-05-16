def	print_data_types():
	number = 42
	str = "42"
	str_char = "quarante-deux"
	fnumber = 42.0
	boolvalue = True
	listnbr = [42]
	dictionarynbr = {
		42: 42
	}
	tuplenbr = (42,)
	print(number, "has a type <class 'int'>")
	print(str, "has a type <class 'str'>")
	print(str_char, "has a type <class 'str'>")
	print(fnumber, "has a type <class 'float'>")
	print(boolvalue, "has a type <class 'bool'>")
	print(listnbr, "has a type <class 'list'>")
	print(dictionarynbr, "has a type <class 'dict'>")
	print(tuplenbr, "has a type <class 'tuple'>")
	print(set(), "has a type <class 'set'>")

print_data_types()