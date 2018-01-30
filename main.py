from ctci import balanced_brackets

if __name__ == "__main__":
    
    #with open('ctci/bb_test79.txt') as f:
    #    f.readline()
    #    for line in f:        
            #print(line, end='\n')
    expression = '{{}('
    
    if balanced_brackets.is_matched(expression) is True:
        print("YES")
    else:
        print("NO")
