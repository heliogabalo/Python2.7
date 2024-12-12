#!/usr/bin/env python

class Fib:
	''' Iterator that yields numbers in the Fibonacci sequence.'''
	
	def __init__(self, max):
		self.max = max
		
	def __iter__(self):
		self.a = 0
		self.b = 1
		return self
		
	def next(self):
		fib = self.a
		if fib > self.max:
			raise StopIteration
		self.a, self.b = self.b, self.a + self.b
		return fib
		
	def myIterator(self, max):
		for n in Fib(max):
			print (n),



		


#from fibonacci import Fib
