# Introduction to Algorithms 6.006 
# Recitation 1

class Static_Array:
	def __init__(self, n):
		self.data = [None] * n
	def get_at(self, i):
		if not (0 <= i < len(self.data)): raise IndexError
		return self.data[i]
	def set_at(self, i, x):
		if not (0 <= i < len(self.data)): raise IndexError
		self.data[i] = x
