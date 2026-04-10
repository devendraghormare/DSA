class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def arrayToLL(arr):
    if not arr:
        return None
    
    head = Node(arr[0])
    curr = head

    for i in range(1, len(arr)):
        temp = Node(arr[i])
        curr.next = temp
        curr = curr.next

    return head


def printLL(head):
    temp = head

    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next 
    
    print("None")

def deleteAllOccurance(head, val):
    while head and head.data == val:
        head = head.next 
    
    temp = head
    prev = None

    while temp:
        if temp.data == val:
            prev.next = temp.next 
        else:
            prev = temp
        
        temp = temp.next 
    return head

head = arrayToLL([1,2,3,4,4,5,6,4])
printLL(deleteAllOccurance(head, 4))


        
