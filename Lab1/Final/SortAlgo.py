import Stack

def Sort(stack1: Stack, stack2: Stack):
    # Sorts elements from stack1 into stack2 in ascending order
    while not stack1.isEmpty():
        temp = stack1.pop()
        
        while not stack2.isEmpty():
            top = stack2.pop()
            
            if top < temp:
                stack1.push(top)  
            else:
                stack2.push(top)
                break

        stack2.push(temp)