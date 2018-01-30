def is_matched(expression):

    left_brackets = ['[', '{', '(']
    right_brackets = {']': '[', '}': '{', ')': '('}

    left_stack = []
    valid = True
    for i in expression.strip():
        if i in left_brackets:
            left_stack.append(i)
        elif i in right_brackets:
            if len(left_stack) == 0:
                valid = False
                break
            item = left_stack.pop()
            if item != right_brackets[i]:
                valid = False
                break
        else:
            print('Invalid character in string ' + expression)
    
    if len(left_stack) > 0:
        valid = False

    return valid

if __name__ == "__main__":
    
    print('balanced brackets')
    #with open('bb_test79.txt') as f:
    #    f.readline()
    #    for line in f:        
            #print(line, end='\n')