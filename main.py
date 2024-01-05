from collections import deque


# (first (list 1 (+ 2 3) 9))

class SExpression(object):

    def __init__(self):
        self.func = None
        self.args = []

    def __str__(self):
        args = [str(x) if isinstance(x, int) else x.__str__() for x in self.args]
        return f"[{self.func} {', '.join(args)}]"

    def __repr__(self):
        return self.__str__()


# very simple validation in order to keep things simple
# only requirement is that input starts with "(" and ends with ")"
# and that there's same number of open and close parentheses
def validate(input):
    if input[0] != "(" or input[-1] != ")":
        raise Exception("Invalid input: expression must start with '(' and end with ')'")

    open_paren = 0
    close_paren = 0

    for char in input:
        if char == "(":
            open_paren += 1
        elif char == ")":
            close_paren += 1

    if open_paren != close_paren:
        raise Exception("Invalid input: number of open and close parentheses must be the same")


def main():
    input = "(first (list 1 (+ 2 3) 9))"

    validate(input)

    # clean up input
    input = input.replace("(", "( ").replace(")", " )").strip().split(" ")

    # clean up unecessary spaces
    input = [x for x in input if x != " "]

    input = deque(input)

    stack = []

    while input:
        token = input.popleft()
        if token == "(":
            stack.append(SExpression())
        elif token == ")":
            s_expr = stack.pop()
            if stack:
                stack[-1].args.append(s_expr)
            else:
                stack.append(s_expr)
        elif token.isnumeric():
            stack[-1].args.append(int(token))
        else:
            stack[-1].func = token      

    s_expr = stack.pop()

    print(s_expr)



if __name__ == '__main__':
    main()
