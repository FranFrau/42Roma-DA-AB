from os import PRIO_USER


class Intern:
	name = "My name? I'm nobody, an intern, I have no name."
	def	builder(self, name):
		if name != "":
			self.name = name

	def	__str__(self):
		return self.name

class Coffee:
	def	__str__(self):
		return "This is the worst coffee you ever tasted."
	
	def	work(self, name):
		raise Exception("I'm just an intern, I can't do that...")
	
	def	make_coffee(self):
		return self
	


intern = Intern()
coffee = Coffee()
intern.builder("Giovanni")
print(intern.__str__())
print(coffee.__str__())
