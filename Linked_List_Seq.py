# Introduction to Aglorithms (6.00.6)
# Notes on Recitation 2 by Simon Norris
# Linked_List_Seq
# Pointer based or 'linked list' implementation of the sequence
# interface. 
# Much more flexible than array-based data structures because 
# their constituent items can be stored anywhere in memory. A
# linked list stores the first element of the list called the
# head of the list, along with the linked list's size, the 
# number of items in the data structure.

class Linked_List_Node:
	# constructor - capable of defining and initializing
	# the class fields
	def __init__(self, x):							# O(1)
		self.item = x
		self.next = None

	# recursive algorithm to link nodes.
	def later_node(self, i):						# O(i)
		if i == 0:  return self
		# - The assert condition statement is something like:
		# 	if condition == true then proceed
		# 	else raise an appropriate error
		# - helps detect problems like type errors by raising early 
		# 	exceptions
		# - works as documentation: confident that the condition holds now
		assert self.next
		return self.next.later_node(i - 1)

class Linked_List_Seq:
	def __init__(self):								# O(1)
		self.head = None
		self.size = 0

	def __len__(self):  return self.size			# O(1)
		
	# https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do-in-python
	# When you call the function, the code written 
	# in the function body does not run. The function 
	# only returns the generator object, then the 
	# function resumes where it left off each time 
	# the for statement uses the generator.
	# The FIRST time the for statement calls the 
	# genenerator object created from the function, 
	# it will run the code in the function from 
	# the beginning until it hits yield, then it 
	# returns the first value of the loop. Then each 
	# subsequent call will run another iteration of 
	# the loop and return the next value. This will 
	# continue until the generator is considered 
	# empty, which happens when the function runs 
	# without hitting yield. 
	# (because the loop comes to an end)
	def __iter__(self): 							# O(n) iter_seq
		node = self.head
		while node:
			yield node.item
			node = node.next

	def build(self, X):								# O(n)
		# maintain 'extrinsic' order of sequence 
		for a in reversed(X):
			self.insert_first(a)

	def get_at(self, i):							# O(i)
		node = self.head.later_node(i)
		return node.item

	def set_at(self, i , x):						# O(i)
		node = self.head.later_node(i)
		node.item = x

	# insert a new first node by first pointing the 
	# new node to the old head of the list and then 
	# updating the lists head pointer to point to 
	# the new node. 
	def insert_first(self, x):						# O(1)
		new_node = Linked_List_Node(x)
		new_node.next = self.head
		self.head = new_node
		self.size += 1

	# delete the first node by updating the list's 
	# head pointer to 'skip over' the old head of 
	# the list - these insert first/last algorithms 
	# are common to all linked-list implementations 
	# and very useful for implementing stacks (FIFO)
	def delete_first(self):							# O(1)
		x = self.head.item
		self.head = self.head.next
		self.size -= 1
		return x

	# insert a new node containing x into position 
	# i in the linked list sequence. 
	def insert_at(self, i, x):						# O(i)
		# adding to the head of a linked list is 
		# elementary - handle this special case
		if i == 0:
			self.insert_first(x)
			return
		# otherwise insert the node at i using
		# Linked_List_Node.later_node(i - 1)
		new_node = Linked_List_Node(x)
		# node is defined and initialized here, 
		# type seems to be inferred:
		node = self.head.later_node(i - 1)
		# node points to the node at (i - 1) now,
		# so insert new node at node.next
		new_node.next = node.next
		# since node points to the node at (i - 1)
		# update node.next to point to the new 
		# node, now stored at position i in the 
		# sequence
		node.next = new_node
		self.size += 1

	# removes the node at position i in the linked 
	# list sequence. Returns x, the data stored in 
	# node(i)
	def delete_at(self, i):							# O(i)
		if i == 0:
			return self.delete_first()
		# node points to node(i - 1)
		node = self.head.later_node(i - 1)
		x = node.next.item  # store the data in node i
		# remove node i (which node.next points to) by 
		# having node.next skip over node i and point to
	    # node(i+1) instead - node(i+1) is accessed by 
		# the pointer node.next.next 
		node.next = node.next.next
		self.size -= 1
		return x  # return the data stored in deleted 
				  # node

	# clears all the data stored in the linked	   # O(n) 
	# list sequence
	def clear(self): self.__init__()

	# wrapper functions                            # O(n)
	def insert_last(self, x):  self.insert_at(len(self), x)
	def delete_last(self):     return self.delete_at(len(self) - 1)
