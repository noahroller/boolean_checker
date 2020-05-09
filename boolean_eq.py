import boolean_simp

'''
Two expressions with the same variables are equal if all possible input combinations
give the same output for each expression. For multiple variables, they are equal if the
output is the same for all possible combinations of common variables. Example: a+b+c and
a++c+d+e both contain a and c. The are only equal if all combinations (0,0), (0,1), (1,0),
and (1,1) for a and c yield the same results between expressions.
*/
'''


def get_expression1():
    pass


def get_expression2():
    pass


def generate_tests():
    pass


variables = {'a': 1, 'b': 0, 'c': 1}
expression = '(a+b+c)'

print(type(variables))
print(type(expression))
boolean_simp.simplify(expression, variables)
print('here')
