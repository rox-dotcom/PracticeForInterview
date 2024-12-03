class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


"""---ZIPPER LIST---"""
# def zipper_List(head1, head2):
#     tail = head1
#     current1= head1.next
#     current2 = head2

#     count = 0

#     while (current1 is not None) and (current2 is not None) :
#         if (count % 2 == 0):
#             #next2 = current2.next
#             tail.next = current2
#             current2 = current2.next
#         else:
#             #next1= current1.next
#             tail.next = current1
#             current1 = current1.next
        
#         tail =  tail.next
#         count += 1
    
#     if(current1 is not None):
#         tail.next = current1
#     if(current2 is not None):
#         tail.next = current2
    

#     return head1  


def zipper_List(head1, head2):#Recursive
    if(head1 is None) and (head2 is None):
        return None
    if(head1 is None):
        return head2
    if(head2 is None):
        return head1
    
    next1 = head1.next
    next2 = head2.next
    head1.next = head2
    head2.next = zipper_List(next1,next2)

    return head1


def main():
    a = Node('A') #list 1
    b = Node('B')
    c = Node('C')
    d = Node('D')

    a.next = b
    b.next = c
    c.next = d
    # a -> b -> c -> d -> none 

    j = Node('J') #list 2
    k = Node('K')
    l = Node('L')

    j.next = k
    k.next = l
    c.next = d

    print(zipper_List(a,j))


if __name__ == '__main__':
    main()