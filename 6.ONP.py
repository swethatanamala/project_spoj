def postfix_helper(a_list):
    result = a_list.pop()
    result = result + a_list.pop()
    result = a_list.pop() + result
    return result

def get_rpn(expr):
    result = []
    i = 0
    while i < len(expr):
        if expr[i] == '(':
            i += 1
        elif expr[i] == ')':
            postfix = postfix_helper(result)
            result.append(postfix)
            i += 1
        else:
            result.append(expr[i])
            i += 1
    return result[0]

t = input()
for _ in range(int(t)):
    expr = input()
    print(get_rpn(expr))