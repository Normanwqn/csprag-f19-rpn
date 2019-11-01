#!/usr/bin/env python3

import operator
operators  = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.floordiv,
}

def calculate(arg):
    stack = list()  # create the stack
    print(arg.split())
    for token in arg.split():
        # print(token)
        try:
             value = int(token)
             stack.append(value)
        except ValueError: # That is an operator
            function = operators[token]
            arg2 = stack.pop()
            print(token)
            arg1 = stack.pop()
            result = function(arg1, arg2)
            stack.append(result)
        #print(stack)
    if len(stack) != 1:
        raise TypeError('malformed input')
    return stack.pop()
def main():
    while True:
        calculate(input("rpn calc> "))


if __name__ == "__main__":
    main()
