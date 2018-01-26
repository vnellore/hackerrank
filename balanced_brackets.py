def is_matched(expression):

    left_brackets = ['[', '{', '(']
    right_brackets = {']': '[', '}': '{', ')': '('}

    left_stack = []
    valid = True
    for i in expression:
        if i in left_brackets:
            left_stack.append(i)
        elif i in right_brackets:
            item = left_stack.pop()
            if item != right_brackets[i]:
                valid = False
                break
        else:
            print('Invalid character in string')

    return valid
