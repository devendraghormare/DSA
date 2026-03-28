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


def evenOddLL(head):
    if not head or not head.next:
        return None
    
############### Brute Force ##################
    
#     temp = head
#     result = []

#     while temp and temp.next:
#         result.append(temp.data)
#         temp = temp.next.next
    
#     if temp:
#         result.append(temp.data)

#     temp = head.next

#     while temp and temp.next:
#         result.append(temp.data)
#         temp = temp.next.next

#     if temp:
#         result.append(temp.data)
    
#     i=0
#     temp = head
#     while temp:
#         temp.data = result[i]
#         i += 1
#         temp = temp.next 
    
#     return head

##################### Optimal approch ###########
    odd = head
    even = head.next 
    evenHead = head.next 

    while even and even.next:
        odd.next = odd.next.next
        even.next = even.next.next

        odd = odd.next
        even = even.next
    
    odd.next = evenHead

    return head

l1 = arrayToLL([1,2,3,4,5])

printLL(evenOddLL(l1))

