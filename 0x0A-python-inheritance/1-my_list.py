#!/usr/bin/python3
"""
contains the MyList class
"""


class MyList(list):
	"""subclass of list"""
	def __init__(self):
		"""initializes the list"""
		super().__init__()

	def print_sorted(self):
		"""prints the list in ascending order"""
		print(sorted(self))
