# Write your solution here
import string
import time

def mov(tableau: dict, coordinate: str, value: str):
    if value in string.ascii_uppercase:
        tableau[coordinate] = tableau[value]
    else:
        tableau[coordinate] = value

def sauter(tableau: dict, variable: str):
    for k, v in tableau.items():
        if v[:-1] == variable:
            return int(k)

def pprint(tableau: dict, coordinate: str):
    if coordinate in string.ascii_uppercase:
        return int(tableau[coordinate])
    else:
        return int(coordinate)

def ajouter(tableau: dict, coordinate: str, value: str):
    if value in string.ascii_uppercase:
        result = int(tableau[coordinate]) + int(tableau[value])
    else:
        result = int(tableau[coordinate]) + int(value)
    tableau[coordinate] = str(result)

def enlever(tableau: dict, coordinate: str, value: str):
    if value in string.ascii_uppercase:
        result = int(tableau[coordinate]) - int(tableau[value])
    else:
        result = int(tableau[coordinate]) - int(value)
    tableau[coordinate] = str(result)

def multiplier(tableau: dict, coordinate: str, value: str):
    if value in string.ascii_uppercase:
        result = int(tableau[coordinate]) * int(tableau[value])
    else:
        result = int(tableau[coordinate]) * int(value)
    tableau[coordinate] = str(result)

def condition(tableau: dict, first_coordinate: str, test_sign: str, second_coordinate: str):
    if first_coordinate in string.ascii_uppercase:
        value_1 = int(tableau[first_coordinate])
    else:
        value_1 = int(first_coordinate)

    if second_coordinate in string.ascii_uppercase:
        value_2 = int(tableau[second_coordinate])
    else:
        value_2 = int(second_coordinate)


    if test_sign == ">":
        if value_1 > value_2:
            return True
        else:
            return False

    if test_sign == ">=":
        if value_1 >= value_2:
            return True
        else:
            return False

    if test_sign == "==":
        if value_1 == value_2:
            return True
        else:
            return False
    if test_sign == "<=":
        if value_1 <= value_2:
            return True
        else:
            return False
    if test_sign == "<":
        if value_1 < value_2:
            return True
        else:
            return False
    
    if test_sign == "!=":
        if value_1 != value_2:
            return True
        else:
            return False


def run(program: list):
    dict_internal_variables = {}
    for l in string.ascii_uppercase:
        dict_internal_variables[l] = 0

    program_steps = {}
    for i, p in enumerate(program):
        program_steps[str(i)] = p

    # Checks if there is an end to the program
    if "END" not in program_steps.values():
        program_steps[str(len(program_steps))] = "END"


    printing_values = []

    step = 0
    while True:
        # print(step)
        actual_step = program_steps[str(step)]

        action = actual_step.split(" ")

        # time.sleep(1)
        # print(action)

        if len(action) == 1:
            p1 = actual_step
            if p1 == "END":
                return printing_values
            elif p1 != "":
                step += 1

        elif len(action) == 2:
            p1, p2 = action
            if p1 == "PRINT":
                printing_values.append(pprint(dict_internal_variables, p2))
                step += 1
            
            if p1 == "JUMP":
                step = sauter(program_steps, p2)

        elif len(action) == 3:
            p1, p2, p3 = action
            if p1 == "MOV":
                mov(dict_internal_variables, p2, p3)
            elif p1 == "ADD":
                ajouter(dict_internal_variables, p2, p3)  
            elif p1 == "SUB":
                enlever(dict_internal_variables, p2, p3)
            elif p1 == "MUL":
                multiplier(dict_internal_variables, p2, p3)
            step += 1

        else:         
            size = len(action)
            if action[0] == "IF":
                p1, p2, p3, p4, p5, p6 =  action
                result = condition(dict_internal_variables, p2, p3, p4)
                if result:
                    if p5 == "JUMP":
                        step = sauter(program_steps, p6)
                else:
                    step += 1

    # print(program_steps)

if __name__ == "__main__":
    program1 = []
    program1.append("MOV A 1")
    program1.append("MOV B 2")
    program1.append("PRINT A")
    program1.append("PRINT B")
    program1.append("ADD A B")
    program1.append("PRINT A")
    program1.append("END")
    result = run(program1)
    print(result)

    program2 = []
    program2.append("MOV A 1")
    program2.append("MOV B 10")
    program2.append("begin:")
    program2.append("IF A >= B JUMP quit")
    program2.append("PRINT A")
    program2.append("PRINT B")
    program2.append("ADD A 1")
    program2.append("SUB B 1")
    program2.append("JUMP begin")
    program2.append("quit:")
    program2.append("END")
    result = run(program2)
    print(result)

    program3 = []
    program3.append("MOV A 1")
    program3.append("MOV B 1")
    program3.append("begin:")
    program3.append("PRINT A")
    program3.append("ADD B 1")
    program3.append("MUL A B")
    program3.append("IF B <= 10 JUMP begin")
    program3.append("END")
    result = run(program3)
    print(result)

    program4 = []
    program4.append("MOV N 50")
    program4.append("PRINT 2")
    program4.append("MOV A 3")
    program4.append("begin:")
    program4.append("MOV B 2")
    program4.append("MOV Z 0")
    program4.append("test:")
    program4.append("MOV C B")
    program4.append("new:")
    program4.append("IF C == A JUMP error")
    program4.append("IF C > A JUMP over")
    program4.append("ADD C B")
    program4.append("JUMP new")
    program4.append("error:")
    program4.append("MOV Z 1")
    program4.append("JUMP over2")
    program4.append("over:")
    program4.append("ADD B 1")
    program4.append("IF B < A JUMP test")
    program4.append("over2:")
    program4.append("IF Z == 1 JUMP over3")
    program4.append("PRINT A")
    program4.append("over3:")
    program4.append("ADD A 1")
    program4.append("IF A <= N JUMP begin")
    result = run(program4)
    print(result)