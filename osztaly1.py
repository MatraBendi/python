class TheSimplestClass:
	osztaly_valt = 10
	def __init__(self):
		self.count = 0
		self.__rejtett__ = 100

my_obj = TheSimplestClass()
print(hasattr(my_obj, 'osztaly_valt'))
print(hasattr(my_obj, 'count'))
print(hasattr(my_obj, '__rejtett__'))
print(hasattr(my_obj, 'bela'))
