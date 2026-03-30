from typing import Optional

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
    if not head:
        return None
    
    temp = head

    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next 
    
    print("None")


def addTwoNumbers(l1: Optional[Node], l2:Optional[Node]):

    dummyNode = Node(-1)
    curr = dummyNode
    carry = 0
    temp1 = l1
    temp2 = l2

    while (temp1 != None or temp2 != None):
        numSum = carry 

        if temp1:
            numSum += temp1.data
            temp1 = temp1.next

        if temp2:
            numSum += temp2.data
            temp2 = temp2.next
        
        newNode = Node(numSum % 10)
        carry = numSum // 10

        curr.next = newNode
        curr = curr.next
    
    if carry:
        newNode = Node(carry)
        curr.next = newNode
    
    return dummyNode.next


l1 = arrayToLL([2,4,3])
l2 = arrayToLL([5,6,4])

printLL(addTwoNumbers(l1, l2))
