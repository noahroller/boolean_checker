import boolean_simp

'''
Two expressions with the same variables are equal if all possible input combinations
give the same output for each expression. For multiple variables, they are equal if the
output is the same for all possible combinations of common variables. Example: a+b+c and
a++c+d+e both contain a and c. The are only equal if all combinations (0,0), (0,1), (1,0),
and (1,1) for a and c yield the same results between expressions.
*/
'''


def set_expression():
    expression = boolean_simp.set_expression()
    return expression


def generate_tests(expression1, expression2):

    #common_char = set(expression1)&set(expression2)

    #common_var = []
    #for elem in common_char:
    #    if elem != '+' and elem != '*' and elem != '(' and elem != ')':
    #        common_var.append(elem)

    #length = len(common_var)

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
    results = []
    for elem in combinations:
        values = list(elem)
        variables = {all_var[i]: int(values[i]) for i in range(len(all_var))}

        results.append(boolean_simp.simplify(expression, variables))

    return results

if __name__ == '__main__':
    print ("Enter two expressions to determine if they are equivalent.")
    expression1 = set_expression()
    expression2 = set_expression()

    combinations, all_var = generate_tests(expression1, expression2)
    results1 = test_expression(expression1, combinations, all_var)
    results2 = test_expression(expression2, combinations, all_var)

    if results1 == results2:
        print("The expressions are equivalent.")
    else:
        print("The expressions are not equivalent.")