#!/usr/bin/env python3.6

class Employee:
	'''
		this is a test demo class
	'''
	classstr = 'this is a test class'
	def __init__(self, name, pay):
		self.name = name
		self.pay = pay
	def hello(self):
		print ('hello' + self.name)

if __name__ == '__main__':
	em  = Employee('小明', 10000)
	print (type(em))
	print (em.hello())
	print (help(Employee))
	
