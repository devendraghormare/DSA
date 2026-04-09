class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def arrayToLL(arr):
    head = Node(arr[0])
    temp = head

    for i in range(1, len(arr)):
        newNode = Node(arr[i])
        temp.next = newNode
        temp = temp.next 
    
    return head

def printLL(head):
    temp = head

    while temp:
        print(temp.data, end=" -> ")
        temp = temp.next 
    
    print("None")


def removeDuplicates(head):
    temp = head

    # while temp and temp.next:
    #     nextNode = temp.next 

    #     while nextNode and nextNode.data == temp.data:
    #         nextNode = nextNode.next 
        
    #     temp.next = nextNode
    #     temp = temp.next 
    
    while temp and temp.next:
        if temp.data == temp.next.data:
            temp.next = temp.next.next 
        else:
            temp = temp.next 
            
    return head

head = arrayToLL([1,2,2,3,3,3,4,4,4,4,5,5,5,5,5])
printLL(removeDuplicates(head))
