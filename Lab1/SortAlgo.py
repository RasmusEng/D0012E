import Stack

def Sort(stack1: Stack, stack2: Stack):
    # Sorts elements from stack1 into stack2 in ascending order
    while not stack1.isEmpty(): # T(n+1) 
        temp = stack1.pop() # T(n)
        
        while not stack2.isEmpty(): # T(n)
            top = stack2.pop() # T(n-1)
            
            if top < temp: # T(n-1)
                stack1.push(top) 
            else: # T(n)
                stack2.push(top) 
                break

        stack2.push(temp) # T(n)
        
        
    # 