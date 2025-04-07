# Introduction to Algorithms 6.0.0.6
# notes on recitation 2 by Simon Norris

# A dynamic array implementation of a sequence, 
# including operations insert_last and delete_last, 
# using table doubling proportions. When attempting 
# to append past the end of the allocation, the 
# contents of the array are transferred to an allocation 
# that is twice as large. When removing down to one 
# fourth of the allocation, the contents of the array 
# are transferred to an allocation that is half as large. 
# The dynamic array allows us to implement insert_last 
# and delete_last in amortized constant time. 
# (see recitation notes for more on amortized constant time)

# https://docs.python.org/3/tutorial/modules.html#
import Array_Sequence

       # inherits from:   modulename.BaseClassName
class Dynamic_Array_Seq(Array_Sequence.Array_Sequence):
	# constructor, defines and initializes class fields.
	# r defines the table proportion, r = 2 for doubling 
	# table proportions
	def __init__(self, r = 2):						# O(1)
		super().__init__()
		self.size = 0
		self.r = r  # table proportion
		self._compute_bounds()
		self._resize(0)

	def __len__(self):  return self.size			# O(1)

	# First yields a generator, which is then used by a 
	# calling for statement to iterate through 
	# self.A[i] using the code in this function.
	def __iter__(self):								# O(n)
		for i in range(len(self)): yield self.A[i]

	# Fills the dynamic array with the contents of X
	# using insert_last
	def build(self, X):								# O(n)
		for a in X: self.insert_last(a)

	#
	def _compute_bounds(self):						# O(1)
		self.upper = len(self.A)
		self.lower = len(self.A) // (self.r * self.r)

	#
	def _resize(self, n):							# O(1) or O(n)
		# no need to resize if array is within bounds
		if (self.lower < n < self.upper): return
		# the new size m, r is the table proportion
		m = max(n, 1) * self.r
		A = [None] * m  # initialize new array 
		# copy the old array into the new array
		self._copy_forward(0, self.size, A, 0) 
		self.A = A # replace the old array with the new array
		self._compute_bounds()  # update bounds for new size

	#
	def insert_last(self, x):						# O(1)amortized
		# check if the array needs resizing
		self._resize(self.size + 1)
		self.A[self.size] = x
		self.size += 1

	#
	def delete_last(self):							# O(1)amortized
		self.A[self.size - 1] = None
		self.size -= 1
		# check if the array needs resizing
		self._resize(self.size)

	#
	def insert_at(self, i, x):						# O(n)
		self.insert_last(None)
		self._copy_backward(i, self.size - (i + 1), self.A, i + 1)
		self.A[i] = x

	# Returns x
	def delete_at(self, i):							# O(n)
		x = self.A[i]  # store x to return
		self._copy_forward(i + 1, self.size - (i + 1), self.A, i)
		self.delete_last()
		return x

	# wrapper functions								# O(n)
	def insert_first(self, x):  self.insert_at(0, x)
	def delete_first(self):     return self.delete_at(0)
