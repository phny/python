#!/usr/bin/env python3.6

import unittest

def my_add_fun(a, b):
	return a + b

def my_sub_fun(a, b):
	return a - b

def my_mul_fun(a, b):
	return a * b

class my_fun_test_case(unittest.case.TestCase):
	'''
	对上面定义的三个函数进行测试
	注意的是：所有的方法必须要以test开头，否则不会被运行
	'''

	def test_add(self):
		result = my_add_fun(1, 2)
		self.assertEqual(result, 3)
	def test_sub(self):
		result = my_sub_fun(3, 1)
		self.assertEqual(result, 2)
	def test_mul(self):
		result = my_mul_fun(4, 2)
		self.assertEqual(result, 8)

if __name__ == '__main__':
	unittest.main()


