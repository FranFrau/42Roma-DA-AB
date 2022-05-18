from week1.ex09.beverages import HotBeverage

class	CoffeeMachine():
	def	__init__(self) -> None:
		pass
	
	class EmptyCup(HotBeverage):
		def	__init__(self, price = 0.9, name = "Empty cup") -> None:
			super().__init__(price, name)
		
		def	description(self):
			return "An empty cup?! Gimme  my money back!"
		
		def	__str__(self):
			return "Empty cup"
	
	class	BrokenMachine(Exception):
		def	__init__(self, message = "This coffee machine has to be repaired") -> None:
			super().__init__(message)

		def	repair(self) -> None:
			pass

		def	serve(self, Coffee) -> None:
			pass