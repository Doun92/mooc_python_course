
def balanced_brackets(my_string: str):
    if len(my_string) == 0:
        return True

    #Remove everything that is not () or [] in string
    only_brackets = "".join([char for char in my_string if char in ["(",")","[","]"]])

    if not (only_brackets[0] == '(' and only_brackets[-1] == ')'):
        if not (only_brackets[0] == '[' and only_brackets[-1] == ']'):
            return False

    # remove first and last character
    return balanced_brackets(only_brackets[1:-1])

if __name__ == "__main__":
    ok = balanced_brackets("(((())))")
    print(ok)

    # there is one closing bracket too many, so this produces False
    ok = balanced_brackets("()())")
    print(ok)

    # this one starts with a closing bracket, False again
    ok = balanced_brackets(")()")
    print(ok)

    # this produces False because the function only handles entirely nested brackets
    ok = balanced_brackets("()(())")
    print(ok)

    ok = balanced_brackets("([([])])")
    print(ok)   #True

    ok = balanced_brackets("(python version [3.7]) please use this one!")
    print(ok)   #True

    # this is no good, the closing bracket doesn't match
    ok = balanced_brackets("(()]")
    print(ok)   #False

    # different types of brackets are mismatched
    ok = balanced_brackets("([bad egg)]")
    print(ok)   #False