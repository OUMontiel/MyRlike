import SemanticCube

quadruples = []

operators = []
operands = []
types = []

results = []
results_types = []

def generateQuadruple(possibleOperators):
    if (len(operators) > 0 and operators[-1] in possibleOperators):
        right_operand = operands.pop()
        right_type = types.pop()
        left_operand = operands.pop()
        left_type = types.pop()
        operator = operators.pop()

        result_type = SemanticCube.semanticCube[SemanticCube.typeNames.index(left_type)][SemanticCube.typeNames.index(right_type)][SemanticCube.operatorNames.index(operator)]
        if (result_type == 'error'):
            print('ERROR: Types mismatch!')
            exit()
        else:
            results.append('t' + str(len(results) + 1))
            results_types.append(result_type)
            quadruples.append([operator, left_operand, right_operand, results[-1]])
            return [results[-1], results_types[-1]]

def generateAssignment():
    if (len(operators) > 0 and operators[-1] == '='):
        right_operand = operands.pop()
        right_type = types.pop()
        left_operand = operands.pop()
        left_type = types.pop()
        operator = operators.pop()

        if (left_type != right_type):
            print('ERROR: Types mismatch!')
            exit()
        else:
            quadruples.append([operator, right_operand, None, left_operand])

def generateReturn(current_function_type):
    return_operand = operands.pop()
    return_type = types.pop()

    if (return_type != current_function_type):
        print('ERROR: Return type does not match function type!')
        exit()
    else:
        quadruples.append(['return', None, None, return_operand])

def generateInput():
    while(len(operators) > 0 and operators[-1] == 'read_write'):
        read_operand = operands.pop()
        operators.pop()

        quadruples.append(['read', None, None, read_operand])

def generateOutput():
    while(len(operators) > 0 and operators[-1] == 'read_write'):
        write_operand = operands.pop()
        operators.pop()

        quadruples.append(['write', None, None, write_operand])
