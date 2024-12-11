"""
Metodo, cadena balanceada

([{}])

in: str 
out: bool

stack
    pop
    peek
    push


    diccionario:
        * ( = a
        * ) = a
        * [ = b
        * ] = b
        * { = c
        * } = c
    
"""


# def Create_stack(stack):
#     stack = []

# def isEmpty(stack):
#     return isEmpty == 0;

# def Push():
#     ingresar elemento
# 
# def Pop():
#   quitar elemento
# 
# def peek() 
#   verificar top elemento
#
# def main()
#    parentes =  '()' 
#    stack = Create_stack()
#     
#    for i in parentes:
#        if i in dicc and dicc[i] not in stack:
#           push(dicc[i])
#        elif dicc[i] alreary in stack:
#           pop(dicc):
#        else:
#            print('No reconozco ese caracter')

from sys import maxsize

def Create_stack():
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
    dicc = { '(': 'a', ')' : 'a', '[' : 'b', ']': 'b', '{': 'c', '}':'c'}

    parentes =  '([])' 
    stack = Create_stack()
    
    for i in parentes:
        try:
            if (i in dicc) and (dicc[i] not in stack):
                push(stack, dicc[i])
            elif dicc[i]  in stack:
                pop(stack)
        except KeyError:
            print('No conozco ese caracter')
    
    if isEmpty(stack):
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    main()
       


