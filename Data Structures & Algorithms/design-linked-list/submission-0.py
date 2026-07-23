class ListNode:

    def __init__(self,val):
        self.val = val
        self.next = None


class MyLinkedList:

    def __init__(self):
        self.head = ListNode(-1)
        self.tail = self.head
        

    def get(self, index: int) -> int:
        i = 0
        curr = self.head
        while i < index and curr:
            i+=1
            curr = curr.next
        
        if curr and curr.next:
            return curr.next.val
        else:
            return -1

        
    def addAtHead(self, val: int) -> None:
        newNode = ListNode(val)
        newNode.next = self.head.next
        self.head.next = newNode

        if self.tail == self.head:
            self.tail = newNode
        
        

    def addAtTail(self, val: int) -> None:
        self.tail.next = ListNode(val)
        self.tail = self.tail.next
        

    def addAtIndex(self, index: int, val: int) -> None:
        i = 0
        curr = self.head
        newNode = ListNode(val)
        while i < index and curr:
            i+=1
            curr = curr.next
        
        if curr and curr.next:
            newNode.next = curr.next
            curr.next = newNode
        

    def deleteAtIndex(self, index: int) -> None:
        i = 0
        curr = self.head
        while i < index and curr:
            i+=1
            curr = curr.next
        
        if curr and curr.next:
            if curr.next == self.tail:
                self.tail = curr
            curr.next = curr.next.next

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)