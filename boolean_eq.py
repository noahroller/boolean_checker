#!/usr/bin/python3.7
import boolean_simp

variables = {'a': 1, 'b': 0, 'c': 1}
expression = '(a+b+c)'

print(type(variables))
print(type(expression))
boolean_simp.simplify(expression, variables)
print('here')
