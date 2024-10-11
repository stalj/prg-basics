#####
# Stack definition
##

stack = []

# add value at the top of the stack
def push(value):
    stack.append(value)

# remove the topmost element of the stack
# and return its value    
def pop():
    if not empty():
        return stack.pop()
    else:
        return None

# return true if the stack is empty
def empty():
    return len(stack) == 0

# display stack
def display():
    for i in range(len(stack)-1,-1,-1):
        print(stack[i])
    print()

if __name__ == "__main__":
    push('First element')
    push('Second element')
    push('Third element')
    display()
    pop()
    display()
    push('Fourth element')
    push('Fifth element')
    display()

