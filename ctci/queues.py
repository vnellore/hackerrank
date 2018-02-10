def peek_dequeue(x, y, peek=False):
    if len(y) == 0:
        if len(x) != 0:
            for i in x:
                y.append(i)
        print(f'y - {y}')

    if len(y) != 0:   
        if peek:
            return y[-1]
        else:
            return y.pop()

def process_commands(cmd_list):
    x,y = [],[]
    print(cmd_list)
    for i in cmd_list:
        print(i)
        cmd_length = len(i.split(' '))
        cmd = i.split(' ')
        if cmd_length == 1:
            if cmd[0] == '2':
                print('dequeue operation')
                print(peek_dequeue(x, y))
                x.clear()
            elif cmd[0] == '3':
                print('peek the front')
                print(peek_dequeue(x, y, True))  
                x.clear()
        elif cmd_length == 2:
            if cmd[0] == '1':
                x.append(cmd[1])
        
if __name__ == '__main__':
    process_commands(['1 42','2','1 14','3','1 28','3','1 60','1 78','2','2'])
