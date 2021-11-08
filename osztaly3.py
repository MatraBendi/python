class Python:
	populacio = 1
	victim = 0
	def __init__(self):
		self.length_ft = 3
		self.__venomous = False
		self.count = 0
	def count(self):
		self.count += 1

class myPython(Python):
	def nyomt(self):
		print(self.count())
