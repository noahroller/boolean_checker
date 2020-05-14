#Boolean Algebra Simplifier - Noah Roller
#Probably a better way to do this, but I'm refreshing some aspects of Python, so I had
#ideas on what I wanted to use

#To do  - allow NOT
#       - limit input

# sets the boolean expression
def set_expression():
    """
    Sets the boolean expression that will be simplified

    :returns:
        string - The inputted boolean expression
    """

    legal = False
    while not legal:
        expression = input('Enter an expression: ')
        if 1 in [i in expression for i in {'+', '*', '(', ')'}] or expression.isalpha():
            legal = True
        else:
            print('Please only enter a-z, +, *, (, )')

    # no special cases once the pre-existing brackets are gone
    expression = '(' + expression + ')'
    return expression


#determines variables needed to be set
def determine_values(expression):
    """
    Finds and returns the unique variables in the expression

    :parameter:
        string expression - The expression being evaluated
    :returns:
        list - The unique variables in the expression
    """
    variables = list(set(expression))
    variables.sort()
    #had issues with normal for loop removal
    variables = filter(lambda i: i != '+' and i != '*' and i != '(' and i != ')', variables)
    return variables


# sets and returns the variable values of a given expression
def set_values(variables):
    """
    Sets the values of the variables given the user input

    :parameter:
        list variables - The list of variables to be set
    :returns:
        dict - Dictionary with variables (string) as keys, values (int) as values
    """

    values = {}
    for key in variables:
        legal = False
        #repeat until legal input is given
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
    """
    Finds the inner-left most brackets of the expression

    :parameter:
        string expression - The expression to find the inner brackets of
    :returns:
        tuple - First and last index of brackets
    """

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
            return i, k

        index = i + 1


# returns the expression in the boundaries given
# can not combine with find_inner_index
def get_bracket(expression, boundary):
    """
        Finds the expression inside the bracket indices given

        :parameter:
            string expression - The expression in the boundaries given
            tuple boundaries - The boundaries of the expression
        :returns:
            string - Expression between the boundaries
        """
    return expression[boundary[0] + 1 : boundary[1]]


# evaluates the value of two variables in a given statement
def evaluate_expression(bracket_exp, values, boundary, expression):
    """
    Simplifies the expression in the boundaries given

    :parameter:
        string expression - The expression in the boundaries given
        tuple boundaries - The boundaries of the expression
    :returns:
        string - Expression between the boundaries
    """

    start = boundary[0]

    # order of operations, AND first
    if bracket_exp.find('*') != -1:
        num = bracket_exp.find('*')
        result = values[bracket_exp[num - 1]] and values[bracket_exp[num + 1]]
        # replace the operand and two variables with the simplified value
        return expression[:start + num] + str(result) + expression[start + num + 3:]
    # OR terms second
    elif bracket_exp.find('+') != -1:
        num = bracket_exp.find('+')
        # OR the terms on each side of the operand
        result = values[bracket_exp[num - 1]] or values[bracket_exp[num + 1]]
        return expression[:start + num] + str(result) + expression[start + num + 3:]
    return str(values[expression[1]])

# returns false if no brackets to remove
def remove_bracket(expression):
    """
       Removes brackets around an expression

       :parameter:
           string expression - The expression to remove brackets from
       :returns:
           string - Expression without the brackets
       """

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
    """
       Yields a result, 1 or 0, given an expression and values

       :parameter:
           string expression - The expression to be simplified
           dict values - The variables of the expression paired with their values
       :returns:
           string - Expression between the boundaries
       """

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
    print('Result:', simplify(expression, values))

