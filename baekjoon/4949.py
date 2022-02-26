while True:
    string = input()
    if string == '.':
        break
    
    stack = list()
    for i in range(len(string)):
        if string[i] == '(' or string[i] == '[':
            stack.append(string[i])
            continue
        
        if string[i] == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            elif len(stack) == 0 or stack[-1] == '[':
                stack.append('none')
        elif string[i] == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            elif len(stack) == 0 or stack[-1] == '(':
                stack.append('none')

    if len(stack) == 0:
        print('yes')
    else:
        print('no')