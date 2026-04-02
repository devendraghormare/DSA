class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def arrayToLL(arr):
    head = Node(arr[0])
    temp = head

    for i in range(1, len(arr)):
        curr = Node(arr[i])
        temp.next = curr
        temp = temp.next 
    
    return head

def reverseLL(head):
    temp = head
    prev = None

    while temp:
        curr = temp.next 
        temp.next = prev
        prev = temp
        temp = curr

    return prev

def isPalindrom(head):
    if not head or not head.next:
        return True
    
################### Brute Force ##############
    # stack = []
    # temp = head

    # while temp:
    #     stack.append(temp.data)
    #     temp = temp.next 
    
    # temp = head

    # while temp:
    #     if temp.data != stack.pop():
    #         return False
        
    #     temp = temp.next 
    
    # return True

    # Time = O(n)
    # Space = O(n)

################### Brute Force ##############

    slow = head
    fast = head

    while fast.next and fast.next.next:
        slow = slow.next 
        fast = fast.next.next 

    newHead = reverseLL(slow.next)
    first = head 
    second = newHead

    while second:
        if first.data != second.data:
            reverseLL(newHead)
            return False
        
        first = first.next 
        second = second.next 
    
    reverseLL(newHead)
    return True

    # Time = O(n)
    # Space = O(1)

head = arrayToLL([1,2,3,2,1])
print(isPalindrom(head))