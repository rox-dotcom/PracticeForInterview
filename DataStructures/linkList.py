
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

"""---PRINT THE LINKED LIST---"""
# def print_linklist(head):
#     current = head #points to the first node

#     while current is not None: #iterates until founds a None, the end of our list
#         print(current.data) 
#         current = current.next
        

def print_linkList(head): #Same function
    if head is None:
        return
    print(head.data)
    print_linkList(head.next) #but w/ recursive



"""---INSERT VALUES IN A ARRAY---"""
# def linkedListToArray(head): #A function to put all nodes in a array
#     values = []
#     current = head
#     while current is not None:
#         values.append(current.data)
#         current = current.next
#     return values

def linkedListToArray(head): #The recusive version of the code
    values = [] #if we don't want to repeat the array
    fillValues(head, values) 
    return values

def fillValues(head, values):
    if head is None:
        return
    values.append(head.data)
    fillValues(head.next, values) #here is the recursion
    
"""---SUM ALL NODES IN LINKLIST---"""
# def sumLinkList(head): #Sums all NODES, into one result 
#     numeroF = 0
#     current = head
#     while current is not None:
#         numeroF += current.data
#         current = current.next
#     return numeroF



def sumLinkList(head): #recoursive
    if(head is None):
        return 0
    return head.data + sumLinkList(head.next) 
#think out of the box, not all problems are the same


"""---Main---"""
def main():
    a = Node(2)
    b = Node(4)
    c = Node(3)
    d = Node(7)

    a.next = b
    b.next = c
    c.next = d
    # a -> b -> c -> d -> none 

    print_linkList(a) #we pass the first node
    #print(linkedListToArray(a))
    #print(sumLinkList(a))
    

if __name__ == '__main__':
    main()