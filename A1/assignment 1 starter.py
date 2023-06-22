class SortedList:
	class Node:
		
		# Node is internal.  Feel free to add
		# to the argument list for its init function if you want
		# you can add additonal data members if you like
		def __init__(self):
			self.data 
			self.next  
			self.prev 

	# Sorted list is external, do not change its prototype.
	# you can add additional data members if you like
	def __init__(self):
		self.front
		self.back 


	def insert(self,data):

	def remove(self,data):

	def is_present(self, data):

	def __len__(self):


	# The functions below called __iter__ and __reversed__ 
	# allows an external function to
	# iterate through your list. 
	#
	# myll = SortedList()
	# 
	# for i in myll:
	#     print(i)
	# 
	# for i in reversed(myll):
	# 	  print(i)
	#
	# with each iteration, curr goes through only one step of the while loop
	# (ie you don't run it all at once..)
	# there are two versions of these function as sentinels nodes do 
	# make a difference in terms of where you start and end
	# keep only the version you are using and erase the version you are 
	# not using (or comment it out...)

	# NOTE: if you change the names of your data members, you need
	# to change them in the functions below or your tests won't pass.

	# This is the version you need if you do not use sentinels:
	def __iter__(self):
		curr = self.front
		while curr:
			yield curr.data
			curr=curr.next

	def __reversed__(self):
		curr = self.back
		while curr:
			yield curr.data
			curr=curr.prev

	# This is the version you need if you used sentinels:
	def __iter__(self):
		curr = self.front.next
		while curr != self.back:
			yield curr.data
			curr=curr.next

	def __reversed__(self):
		curr = self.back.prev
		while curr != self.front:
			yield curr.data
			curr=curr.prev