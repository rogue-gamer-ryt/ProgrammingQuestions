"""
A string is said to be an arithmetical expression in Reverse Polish notation (RPN) if:
(1.) It is a single digit or a sequence of digits, prefixed with an option -, c.g.,"6" , "129" ,"-42".
(2.) It is of the form "A,B,o" where A and B are RPN expressions and o is one of +, -,x, /.
For example, the following strings satisfy these rules: "1729", "3,4,+,2,x,L,+", "1.,1.,+,-2,x,',
"-641,,6, 1,28, 1".

An RPN expression can be evaluated uniquely to an integer, which is determined recursively.
The base case corresponds to Rule (1.), which is an integer expressed in base-lO positional system.
Rule (2.)corresponds to the recursive case, and the RPNs are evaluated in the natur alway, e.g., it A
evaluates to 2 and B evaluates to 3, then "A,B,x" evaluates to 6.

Write a program that takes an arithmetical expression in RPN and retums the number that the
expression evaluates to.
"""
# Store the partial results after performing an operation in stack

def evaluate(RPN_expression):
    intermediate_resuls = []
    DELIMITER = ','
    OPERATORS = {
        '+': lambda y, x: x + y,
        '-': lambda y, x: x - y,
        '*': lambda y, x: x * y,
        '/': lambda y, x: int(x / y)
    }

    for token in RPN_expression.split(DELIMITER):
        if token in OPERATORS:
            intermediate_resuls.append(
                OPERATORS[token](intermediate_results.pop(), intermediate_results.pop())
            )
        else:
            intermediate_results.append(int(token))
    
    return intermediate_results[-1]
