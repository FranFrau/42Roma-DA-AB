from random import random, randrange
from beverages import Cappuccino, Chocolate, Coffee, HotBeverage, Tea

class	CoffeeMachine():
	def	__init__(self) -> None:
		self.uses = 0
	
	class EmptyCup(HotBeverage):
		def	__init__(self, price = 0.9, name = "Empty cup") -> None:
			super().__init__(price, name)
		
		def	description(self):
			return "An empty cup?! Gimme  my money back!"
		
		def	__str__(self):
			return "Empty cup"
	
	class	BrokenMachineException(Exception):
		def	__init__(self, message = "This coffee machine has to be repaired") -> None:
			super().__init__(message)

	def	repair(self) -> None:
		self.uses = 0

	def	serve(self, drink) -> None:
		if (self.uses == 10):
			return self.BrokenMachineException()
		self.uses += 1
		random_number = randrange(6)
		if random_number == 4:
			return CoffeeMachine.EmptyCup()
		return drink
