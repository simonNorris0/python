# Introduction to Algorithms 6.00.6
# notes on recitation 3 by simon norris

# Selection sort maintains and grows a subset of
# the largest i items in sorted order. 
# "in-place" algorithm: can be implemented using
# at most a constant amount of additional space. 
# The only operations performed on the array 
# are comparisons and swaps.
# (selection sort is not "stable")
def selection_sort(A):						# Selection sort array A
	# first parameter is the initial value
	# second parameter is the final value
	# third parameter is the step amount
	# loop backwards
	for i in range(len(A) - 1, 0, -1)		# O(n) loop over array
		# m for 'max value'
		m = i								# O(1) initial index of max
		for j in range(i):					# O(i) search for max in A[:i]
			if A[m] < A[j]:					# O(1) check for larger value
				m = j						# O(1) new max found
		A[m], A[i] = A[i], A[m]				# O(1) swap

# Insertion sort maintains and grows a subset of
# the first i input items in sorted order. 
# "in-place" algorithm: can be implemented using 
# at most a constant amount of additional space.
# The only operations performed on the array 
# are comparisons and swaps
# Insertion sort is "stable" meaning that 
# items having the same value will appear in 
# the sort in the same order they appeared 
# in the input array.
def insertion_sort(A):						# Insertion sort array A
	# loop forwards
	for i in range(1, len(A)):				# O(n) loop over array
		j = i								# O(1) initialize pointer
		while j > 0 and A[j] < A[j - 1]:	# O(i) loop over prefix
			A[j - 1], A[j] = A[j], A[j - 1] # O(1) swap
			j = j - 1						# O(1) decrement j

#
def merge_sort(A, a = 0, b = None):			# Sort sub-array A[a:b]
