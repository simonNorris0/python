# Introduction to Aglorithims 6.00.6
# Notes on recitation 3 by Simon Norris

# Implements a set with a sorted array, where the item with 
# the smallest key appears first (at index 0), and the item 
# with the largest key appears last. Sorting enables us to 
# use binary search to find keys and support Order operations

import Array_Sequence()

class Sorted_Array_Set:
	def __init__(self):    self.A = Array_Sequence()	# O(1)
	def __len__(self):     return len(self.A)			# O(1)
	def __iter__(self):    yield from self.A			# O(n)
	def iter_order(self):  yield from self				# O(n)

	# but how do we sort the array?
	def build(self, X):									# O(?)
		self.A.build(X)
		self._sort()

	def _sort (self):									# O(?)
		??

	# https://en.wikipedia.org/wiki/Binary_search#Algorithm
	# Binary search works on sorted arrays. Binary search 
	# begins by comparing an element in the middle of the 
	# array with the target value. If the target value 
	# matches the element, its position in the array is 
	# returned. If the target value is less than the 
	# element, the search continues in the lower half of 
	# the array. If the target value is greater than the 
	# element, the search continues in the upper half 
	# of the array. The algorithm eliminates the half 
	# of the remaining array in which the target value 
	# cannot lie in each iteration. 
	#
	# Given an array A of n elements sorted such that 
	# A[0] <= A[1] <= A[2] <= ... <= A[n-1], and target
	# value T, the following subroutine uses binary search 
	# to find the index of T in A:
	#
	# 1. Set L to 0 and R to (n - 1)
	# 2. If L > R, the search terminates as unsuccessful
	# 3. Set m (the position of the middle element) to 
	#    the floor of ((L + R) / 2), which is the 
	#	 greatest integer less than or equal to 
	#	 ((L + R) / 2)
	# 4. If A[m] < T, set L to (m + 1) and go to step 2
	# 5. If A[m] > T, set R to (m - 1) and go to step 2
	# 6. Now A[m] = T, the search is successful;
	#	 return m
	# 
	# This recursive procedure keeps track of the search 
	# boundaries with the two variables L and R.
	#
	# Implements the binary search algorithm with 
	# parameters k == T (target value), i == L, 
	# and j == R. 
	# Returns the position of the target value in the 
	# sorted array when successful, returns the value 
	# of the current lower search boundary when unsuccessful. 
	def _binary_search(self, k, i, j):					# O(log n)
		# base case, when the search boundaries have constrained
		if i >= j:         return i  # unsuccessful search
		# find the position/data of the middle element in the array
		m = (i + j) // 2             # floor division: //
		x = self.A.get_at(m)
		# search proceeds to lower half (recurses) 
		if x.key > k:      return self._binary_search(k, i, m - 1)
		# search proceeds to upper half (recurses)
		if x.key < k:      return self._binary_search(k, m + 1, j)
		return m					 # successful search

	# Returns the data in the minimum value stored in 
	# the sorted array (the first element)
	def find_min(self):									# O(1)
		if len(self) > 0:  return self.A.get_at(0)
		else:              return None

	# Returns the data in the maximum value stored in 
	# the sorted array (the last element)
	def find_max(self):									# O(1)
		if len(self) > 0:  return self.A.get_at(len(self) - 1)
		else:              return None

	# Uses _binary_search to find the target value k 
	# in the sorted array. _binary_search is called with 
	# search boundaries L == 0 and R == len(self) - 1
	# (to set the initial search boundaries to include 
	#  the entire array)
	# Returns the data stored at the target key, if 
	# the key is stored in the sorted array.
	# Returns None if the key is not stored in the 
	# sorted array
	def find(self, k):									# O(log n)
		if len(self) == 0:    return None
		i = self._binary_search(k, 0, len(self) - 1)
		x = self.A.get_at(i)
		if x.key == k:        return x
		else:                 return None

	# Uses _binary_search to find the target value k 
	# in the sorted array. L == 0, R == len(self) - 1
	# Returns the next value after k stored in the 
	# sorted array according to the set's order.
	def find_next(self, k):								# O(log n)
		if len(self) == 0:    return None
		i = self._binary_search(k, 0, len(self) - 1)
		x = self.A.get_at(i)
		if x.key > k:         return x
		if i + 1 < len(self): return self.A.get_at(i + 1)
		else:                 return None

	# Uses _binary_search to find the target value k
	# in the sorted array. L == 0, R == len(self) - 1
	# Returns the value stored before k in the 
	# sorted array according to the set's order.
	def find_prev(self, k):								# O(log n)
		if len(self) == 0:    return None
		i = self._binary_search(k, 0, len(self) - 1)
		x = self.A.get_at(i)
		if x.key < k:         return x
		if i > 0:             return self.A.get_at(i - 1)
		else:                 return None

	# Insert data x into the sorted array set. Sorted 
	# array sets cannot hold duplicate keys. Returns True 
	# when successful and false when unsuccsessful
	# [~ when unsuccessful the pre-existing key is still 
	# [  replaced with the new data insert() was called 
	#    to insert into the array set ]
	def insert(self, x):								# O(n)
		# special case: inserting into an empty array
		if len(self.A) == 0:
			self.A.insert_first(x)
		else:
			# _binary_search returns either:
			#  - the position of the target value in the
			#  sorted array or
			#  - the value of the lower search boundary 
			#  when the function exited: this is the 
			#  position of the greatest value smaller 
			#  than the target value (a.k.a the previous 
			#  item in the set)
			i = self._binary_search(x.key, 0, len(self.A) - 1)
			k = self.A.get_at(i).key
			# ** the set interface does not allow duplicate keys **
			if k == x.key:
				self.A.set_at(i, x) # update the data stored at i
				return False        # unsuccessful insert
			# if the key returned by binary search is greater than 
			# the key to insert, insert the new value at the 
			# position of the returned key.  
			if k > x.key:    self.A.insert_at(i, x)
			# otherwise the key returned by binary search is 
			# less than the key to insert, insert the new value 
			# next after the position of the returned key (i + 1)
			else:            self.A.insert_at(i + 1, x)
		return True					# successful insert

	# Delete the data (and key) stored at a given key k in the 
	# sorted array set. Returns the data stored in A[k] 
	def delete(self, k):								# O(n)
		# search / load the data to delete
		i = self._binary_search(k, 0, len(self.A) - 1)
		# prove that the data to delete exists
		assert self.A.get_at(i).key == k
		return self.A.delete_at(i)
