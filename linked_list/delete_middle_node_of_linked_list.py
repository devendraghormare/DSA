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

def deleteMiddle(head):
    if not head or not head.next:
        return None
################# Brute Force #################
    # count = 0
    # temp = head

    # while temp:
    #     count += 1
    #     temp = temp.next 
    
    # delNode = count // 2 
    # print(delNode)

    # temp = head
    # for _ in range(delNode - 1):
    #       temp = temp.next
    
    # temp.next = temp.next.next 

    # return head

############## Optimal approach ############
    slow = head
    fast = head
    prev = None

    while fast and fast.next :
        prev = slow
        slow = slow.next 
        fast = fast.next.next 
    
    prev.next = prev.next.next 
    return head

head = arrayToLL([1,2,3,4,5])
printLL(deleteMiddle(head))