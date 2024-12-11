from sys import maxsize

def createStak():
    stack = []
    return stack

def isEmpty(stack):
    return len(stack) == 0

def push(stack, item):
    stack.append(item)
    print(item + " pushed to stack")

def pop(stack):
    if(isEmpty(stack)):
        return str(-maxsize - 1)
    return stack.pop()

def peek(stack):
    if(isEmpty(stack)):
        return str(-maxsize - 1)
    return stack[len(stack)-1]


def main():
    stack = createStak()
    push(stack, str(10))
    push(stack, str(20))
    push(stack, str(30))
    push(stack, str(40))

    print(peek(stack)+ " is The top element")
    print(pop(stack)+ " popped from stack")
    print(peek(stack)+ " is The top element")



if __name__ == '__main__':
    main()