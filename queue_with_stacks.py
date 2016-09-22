print "Hello"

def enqueue(stack1, stack2, e):
    stack1.append(e)

def dequeue(stack1, stack2, e):
    if len(stack2) == 0
        stack2.extend(stack1)
        stack1.clear()
    
    if len(stack2) > 0
        return stack2.pop()

    raise Exception('Trying to dequeue an empty queue')
