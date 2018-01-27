from ctci import balanced_brackets

if __name__ == "__main__":

    t = 1
    for a0 in range(t):
        expression = '({(){}[]})[]'
        if balanced_brackets.is_matched(expression) is True:
            print("YES")
        else:
            print("NO")
