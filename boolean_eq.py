import boolean_simp

#Boolean Algebra Equivalence Checker - Noah Roller


def generate_tests(expression1, expression2):
    """
    Generates a list of tests to test the expression in the format of
    ['000','001','010',...] <- for three variables

    :parameter:
        string expression1 - The first expression being evaluated
        string expression1 - The second expression being evaluated
    :returns:
        list - List of strings containing the test values
        list - List of all variables in expression
    """

    all_char = set(expression1+expression2)

    all_var = []
    #removes +, *, (, )
    for elem in all_char:
        if elem != '+' and elem != '*' and elem != '(' and elem != ')':
            all_var.append(elem)
    all_var.sort() #easier debugging

    length = len(all_var)
    combinations = []
    for i in range(0, 2**length):
        #converts to binary and removes 0b from binary number
        #maintains a specific number of leading zero
        combinations.append(("{0:b}".format(i)).zfill(length))

    return combinations, all_var


def test_expression(expression, combinations, all_var): #could determine all_var from expression if need be
    """
    Tests the expression using the combinations

    :parameter:
        string expression - The expression being tested
        list combinations - List of combination strings, must containing leading zeros
        list all_var - Set of all variables in the two expressions
    :returns:
        list - Results of all the tests of the expression
    """

    results = []
    for elem in combinations:
        values = list(elem)
        variables = {all_var[i]: int(values[i]) for i in range(len(all_var))}

        results.append(boolean_simp.simplify(expression, variables))

    return results

if __name__ == '__main__':
    print("Enter two expressions to determine if they are equivalent.")
    print("NOT is currently not supported, will be added later.")
    expression1 = boolean_simp.set_expression()
    expression2 = boolean_simp.set_expression()

    combinations, all_var = generate_tests(expression1, expression2)
    results1 = test_expression(expression1, combinations, all_var)
    results2 = test_expression(expression2, combinations, all_var)

    if results1 == results2:
        print("The expressions are equivalent.")
    else:
        print("The expressions are not equivalent.")