class HotBeverage:
	price = 0.30
	name = "Hot beverage"
	def description(self):
		return "Just some hot water in a cup"
	def __str__(self):
		print("name :", self.name, "\nprice :", self.price, "\ndescription :", self.description())

idk = HotBeverage()
idk.__str__()