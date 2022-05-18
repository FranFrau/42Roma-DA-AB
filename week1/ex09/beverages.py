class	HotBeverage:
	def	__init__(self, price = 0.30, name = "Hot beverage") -> None:
		self.price = price
		self.name = name

	def	description(self):
		return "Just some hot water in a cup"

	def	__str__(self):
		return "name : " + self.name + "\nprice : " + str(self.price) + "\ndescription : " + self.description()

class	Coffee(HotBeverage):
	def	__init__(self, price=0.4, name="coffee") -> None:
		super().__init__(price, name)

	def	description(self):
		return "A coffee, to stay awake"

class	Tea(HotBeverage):
	def	__init__(self, price=0.3, name="tea") -> None:
		super().__init__(price, name)

	def	description(self):
		return "Just some hot water in a cup"

class	Chocolate(HotBeverage):
	def	__init__(self, price=0.5, name="chocolate") -> None:
		super().__init__(price, name)

	def	description(self):
		return "Chocolate, sweet chocolate..."

class	Cappuccino(HotBeverage):
	def	__init__(self, price=0.45, name="cappuccino") -> None:
		super().__init__(price, name)

	def	description(self):
		return "Un po' di Italia nella sua tazza!"
