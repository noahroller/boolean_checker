import re

'''
Boolean Algebra Simplifier - Noah Roller
Probably a better way to do this, but I had certain parts of python I wanted to use
'''


# sets the boolean expression
def set_expression():
    legal = False
    while not legal:
        expression = input('Enter an expression: ')
        if 1 in [i in expression for i in {'+', '*', '(', ')'}] or re.match("^[a-z]*$", expression):
            legal = True
        else:
            print('Please only enter a-z, +, *, (, )')

    # no special cases once the pre-existing brackets are gone
    expression = '(' + expression + ')'
    return expression


#determines variables needed to be set
def determine_values(expression):
    variables = list(set(expression))
    variables.sort()
    #had issues with normal for loop removal
    variables = filter(lambda i: i != '+' and i != '*' and i != '(' and i != ')', variables)
    return variables


# sets and returns the variable values of a given expression
def set_values(variables):
    values = {}
    for key in variables:
        legal = False
        while not legal:
            values[key] = input('Set the value of ' + key + ': ')
            if values[key] == '0' or values[key] == '1':
                values[key] = int(values[key])
                legal = True
            else:
                print("Please enter a '0' or '1'")

    return values


# finds and returns a list of the inner and left most brackets in the expression
def find_inner_bracket(expression):
    index = 0
    length = len(expression)
    # searches each index for a '(' in which the next bracket is a ')'
    while index < length:
        i = expression.find('(', index)
        if i == -1:
            return 0

        j = expression.find('(', i + 1)
        k = expression.find(')', i + 1)

        if k < j or j == -1:
            return [i, k]

        index = i + 1


# returns the expression in the boundaries given
# can not combine with find_inner_index
def get_bracket(expression, boundary):
    return expression[boundary[0] + 1:boundary[1]]


# evaluates the value of two variables in a given statement
def evaluate_expression(bracket_exp, values, boundary, expression):
    start = boundary[0]

    # order of operations, AND first
    if bracket_exp.find('*') != -1:
        num = bracket_exp.find('*')
        # AND the terms on each side of the operand
        result = and_gate(values[bracket_exp[num - 1]], values[bracket_exp[num + 1]])
        # replace the operand and two variables with the simplified value
        return expression[:start + num] + str(result) + expression[start + num + 3:]
    # OR terms second
    elif bracket_exp.find('+') != -1:
        num = bracket_exp.find('+')
        # OR the terms on each side of the operand
        result = or_gate(values[bracket_exp[num - 1]], values[bracket_exp[num + 1]])
        return expression[:start + num] + str(result) + expression[start + num + 3:]
    return str(values[expression[1]])

# AND gate
def and_gate(a, b):
    if a == 1 and b == 1:
        return 1
    else:
        return 0


# OR gate
def or_gate(a, b):
    if a == 1 or b == 1:
        return 1
    else:
        return 0


# returns false if no brackets to remove
def remove_bracket(expression):
    length = len(expression)
    index = 0
    while index < length:
        i = expression.find('(', index)
        if i == -1:
            break

        if expression[i + 2] == ')':
            expression = expression[:i] + expression[i + 1] + expression[i + 3:]

        index = i + 1
    return expression


# values -> dictionary of variables
def simplify(expression, values):
    values['0'] = 0
    values['1'] = 1

    while len(expression) > 1:
        if expression.find('(') != -1:
            bracket = find_inner_bracket(expression)
            inside_bracket = get_bracket(expression, bracket)
            result = evaluate_expression(inside_bracket, values, bracket, expression)
            expression = remove_bracket(result)
    return expression


if __name__ == '__main__':
    expression = set_expression()
    values = set_values(determine_values(expression))
    print(expression)
    print(values)
    print(simplify(expression, values))

