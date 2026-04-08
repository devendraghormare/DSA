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

def reverseLL(head):
    temp = head
    prev = None

    while temp:
        curr = temp.next 
        temp.next = prev
        prev = temp 
        temp = curr
    
    return prev

def recursionFun(temp):
    if temp == None:
        return 1
    
    carry = recursionFun(temp.next)
    temp.data += carry
    if temp.data < 10:
        return 0
    temp.data = 0
    return 1

def addOneToLL(head):
################# Brute Force ###############
    # head = reverseLL(head)
    # temp = head
    # carry = 1

    # while temp:
    #     temp.data += carry

    #     if temp.data < 10:
    #         carry = 0
    #         break
    #     else:
    #         temp.data = 0
    #         carry = 1
        
    #     temp = temp.next 
    
    # if carry == 1:
    #     newNode = Node(1)
    #     head = reverseLL(head)
    #     newNode.next = head
    #     return newNode
    # else:
    #     head = reverseLL(head)
    #     return head
    
    # Time = O(3n) = O(n)
    # Space = O(1) 

######################## Optimal solution - recursion #######################
    carry = recursionFun(head)
    if carry == 1:
        newNode = Node(1)
        newNode.next = head
        head = newNode
    
    return head

    # Time = O(n)
    # Space = O(n) --recursive stack space


# head = arrayToLL([1,5,9])
head = arrayToLL([9,9,9,9])
printLL(addOneToLL(head))
