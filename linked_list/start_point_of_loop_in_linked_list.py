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
        

def findStartPointInLoopOfLL(head):
    if not head or not head.next:
        return None
################ Brute Force ################
    # mpp = {}
    # temp = head

    # while temp:
    #     if temp in mpp:
    #         return temp
        
    #     mpp[temp] = 1
    #     temp = temp.next 
    
    # return None

    # Time - O(n)
    # Space - O(n)
################ optimal approach ################
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next 
        fast = fast.next.next 

        if slow == fast:
            slow = head
            while slow != fast:
                fast = fast.next 
                slow = slow.next 

            return slow
    
    return None

    # Time - O(n)
    # Space - O(1)
head = arrayToLL([3,2,0,-4])

temp = head
second = head.next

while temp.next:
    temp = temp.next

temp.next = second

result = findStartPointInLoopOfLL(head)
if result:
    print(result.data)
else:
    print("No cycle")

