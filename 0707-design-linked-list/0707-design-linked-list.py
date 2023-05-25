class Node:
    def __init__(self, value = None):
        self.value = value
        self.next = None
        
class MyLinkedList:

    def __init__(self):
        self.head = None
        self.tail = None
        

    def get(self, index: int) -> int:
        cur = self.head
        i = 0
        while index > i and cur:
            cur = cur.next
            i += 1
        if cur:
            return cur.value
        else:
            return -1
        

    def addAtHead(self, val: int) -> None:
        add = Node(val)
        if not self.head:
            self.head = add
            self.tail = add
        else:
            add.next = self.head
            self.head = add           
        

    def addAtTail(self, val: int) -> None:
        add = Node(val)
       
        if not self.head:
            self.head = self.tail = add
            
        else:
            self.tail.next = add
            self.tail = add
        

    def addAtIndex(self, index: int, val: int) -> None:
        if index == 0:
            self.addAtHead(val)
        else:
            add = Node(val)
            i = 0
            cur = self.head
            while i < index - 1 and cur:
                cur = cur.next
                i += 1
            if cur:
                add.next = cur.next
                cur.next = add
                if not add.next:
                    self.tail = add

    def deleteAtIndex(self, index: int) -> None:
        if index == 0:
            self.head = self.head.next
        
        else:
            cur = self.head
            i = 0
            while i < index - 1 and cur:
                i += 1
                cur = cur.next
            if cur and cur.next:
                cur.next = cur.next.next
                if not cur.next:
                    self.tail = cur


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)