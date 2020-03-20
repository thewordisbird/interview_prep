import operator

def rpn(expression):
    operands = []
    operators = {'+':operator.__add__ ,'-': operator.__sub__ , '/': operator.__truediv__, '*': operator.__mul__ }
    # Assume expression is always valid as stated in problem
    for item in expression:
        if item in operators:
            result = evaluate(operands.pop(), operands.pop(), operators[item])
            operands.append(result)
        else:
            operands.append(item)
    
    return operands.pop()

def evaluate(right, left, op):
    return op(left, right)
        
if __name__ == "__main__":
    expression =  [15, 7, 1, 1, '+', '-', '/', 3, '*', 2, 1, 1, '+', '+', '-']
    #expression =  [15, 7, '-']
    print(rpn(expression))