class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

"""---FIND IN LINKLIST---"""

# def findInList(head,target):
#     current = head
#     while current is not None:
#         if current.data == target:
#             return True
#         current = current.next
#     return False
        


def findInList(head, target):
    if (head is None):
        return False
    if(head.data == target):
        return True
    return findInList(head.next,target)


"""---INDEX OF THE NODE---""" 

# def indexMatch(head, target):
#     current = head
#     count = 0

#     while current is not None:
#         if target == count:
#             return current.data
#         count += 1
#         current = current.next
#     return None


def indexMatch(head, target): #In this recursive example, we count on backwards, 
    if(head is None):         #so like from the target 2 until 0
        return None
    if(target == 0): 
        return head.data
    return indexMatch(head.next, target - 1)


"""---REVERSE LIST---""" 

def reverse_list(head):
    prev = None
    current = head
    while(current is not None):
        next = current.next
        current.next = prev
        prev = current
        current = next
    return prev.data


# def reverse_list(head, prev = None):
#     if(head is None):
#         return prev
#     next = head.next
#     head.next = prev
#     return reverse_list(next, head) #here is the recursive part 




"""---Main---"""
def main():
    a = Node('A')
    b = Node('B')
    c = Node('C')
    d = Node('D')

    a.next = b
    b.next = c
    c.next = d
    # a -> b -> c -> d -> none 


    #print(findInList(a,'F'))
    #print(indexMatch(a, 2))
    #print(reverse_list(a))


if __name__ == '__main__':
    main()