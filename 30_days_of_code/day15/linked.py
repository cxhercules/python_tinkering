class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class Solution:
    def display(self,head):
        current = head
        while current:
            print(current.data,end=' ')
            current = current.next

    def insert(self,head,data):
    #Complete this method
        #print (head)
        if head == None:
            myNode = Node(data)
            head = myNode
        else:
            last = head
            while last.next:
                last = last.next
            myNode = Node(data)
            last.next = myNode
        return head

mylist= Solution()
T=int(input())
head=None
for i in range(T):
    data=int(input())
    head=mylist.insert(head,data)
mylist.display(head);
