

def process_commands(cmd_list):
    print(cmd_list)
    for i in cmd_list:
        print(i)
        cmd_length = len(i.split(' '))
        cmd = i.split(' ')
        if cmd_length == 1:
            if cmd[0] == '2':
                print('dequeue operation')
            elif cmd[0] == '3':
                print('peek the front')
            
        elif cmd_length == 2:
            if cmd[0] == '1':
                print('enqueue operation')


if __name__ == '__main__':
    process_commands(['1 42','2','1 14','3','1 28','3','1 60','1 78','2','2'])
