#!/usr/bin/python3.7
import re

#Boolean Algebra Simplifier - Noah Roller
#Probably a better way to do this, but I had certain parts of python I wanted to use

#sets the boolean expression
def set_expression():
    legal = False
    while not legal:
        expression = input('Enter an expression: ')
        if 1 in [i in expression for i in {'+', '*', '(', ')'}] or re.match("^[a-z]*$", expression):
            legal = True
        else: print('Please only enter a-z, +, *, (, )')

    #no special cases once the pre-existing brackets are gone
    expression = '(' + expression + ')'
    return expression

#sets and returns the variable values of a given expression
def set_values(expression):
    global values
    variables = list(set(expression))
    variables.sort()
    variables = filter(lambda i: i != '+' and i != '*' and i != '(' and i != ')', variables)

    values = {}
    for key in variables:
        legal = False
        while not legal:
            values[key] = input('Set the value of ' + key + ': ')
            if re.match("^[01]*$", values[key]) and values[key] is not None:
                legal = True
            else: print("Please enter a '0' or '1'")

    values['0'] = 0
    values['1'] = 1
    return values

#finds and returns a list of the inner and left most brackets in the expression
def find_inner_bracket(expression):
	index = 0
	length = len(expression)
    #searches each index for a '(' in which the next brack is a ')'
	while index < length:
		i = expression.find('(', index)
		if i == -1:
			return 0
		
		j = expression.find('(', i + 1)
		k = expression.find(')', i + 1)
		
		if k < j or j == -1:
			return [i, k]

		index = i + 1


#returns the expression in the boundries given
def get_bracket(expression, boundry):
    return expression[boundry[0]+1:boundry[1]]

#evaluates the value of two variables in a given statement
def evaluate_expression(bracket_exp, values, boundry, expression):
    start = boundry[0]

    #order of operations, AND first
    if bracket_exp.find('*') != -1:
        num = bracket_exp.find('*')
        #AND the terms on each side of the operand
        result = and_(values[bracket_exp[num-1]], values[bracket_exp[num+1]])
        #replace the operand and two variables with the simplified value
        return expression[:start+num] + str(result) + expression[start+num+3:]
    #OR terms second
    elif bracket_exp.find('+') != -1:
        num = bracket_exp.find('+')
        #OR the terms on each side of the operand
        result = or_(values[bracket_exp[num-1]], values[bracket_exp[num+1]])
        return expression[:start+num] + str(result) + expression [start+num+3:]


#AND gate, true -> 1, false -> 0
def and_(a, b):
    if a and b:
        return 1
    else: return 0


#OR gate, true -> 1, false -> 0
def or_(a, b):
    if a or b:
        return 1
    else: return 0


#returns false if no brackets to remove
def remove_bracket(expression):
    length = len(expression)
    index = 0
    while index < length:
        i = expression.find('(', index)
        if i == -1:
            break

        if expression[i+2] == ')':
            expression = expression[:i] + expression[i+1] + expression[i+3:]

        index = i + 1
    return expression


#values -> dictionary of variables
def simplify(expression,values):
    while len(expression) > 1:
        if expression.find('(') != -1:
            bracket = find_inner_bracket(expression)
            inside_bracket = get_bracket(expression, bracket)
            result = evaluate_expression(inside_bracket, values, bracket, expression)
            expression = remove_bracket(result)
    print('result: ' + expression)

values = {}
values['a'] = 1
values['b'] = 1
values['c'] = 0
values['d'] = 1
values['0'] = 0
values['1'] = 1

simplify('((a*c+d)+(b*d))',values)