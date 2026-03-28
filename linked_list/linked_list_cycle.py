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

def hasCycle(head):

############# Brute Force ###########
    # mpp = {}
    # temp = head

    # while temp:
    #     if temp in mpp:
    #         return True
        
    #     mpp[temp] = 1
    
    # return False

# Time = O(n)
# Space = O(n)

############## Optimal approach ###########

    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 

        if slow == fast:
            return True
    
    return False

# Time = O(n)
# Space = O(1)

head = arrayToLL([3,2,0,-4])
# create cycle: last node points to second node
temp = head
second = head.next

while temp.next:
    temp = temp.next

temp.next = second   # cycle created

print(hasCycle(head))   # now should be True