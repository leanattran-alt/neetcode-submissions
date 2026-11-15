from typing import List

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class LinkedList:
    def __init__(self):
        self.head = ListNode()
        self.tail = self.head
        self.size = 0

    def get(self, i: int) -> int:
        if i < 0 or i >= self.size:
            return -1

        curr = self.head.next
        for _ in range(i):
            curr = curr.next

        return curr.val

    def insertHead(self, val: int) -> None:
        node = ListNode(val, self.head.next)
        self.head.next = node

        if self.size == 0:
            self.tail = node

        self.size += 1

    def insertTail(self, val: int) -> None:
        node = ListNode(val)
        self.tail.next = node
        self.tail = node
        self.size += 1

    def remove(self, i: int) -> bool:
        if i < 0 or i >= self.size:
            return False

        prev = self.head
        for _ in range(i):
            prev = prev.next

        removed = prev.next
        prev.next = removed.next

        if removed == self.tail:
            self.tail = prev

        self.size -= 1
        return True

    def getValues(self) -> List[int]:
        result = []
        curr = self.head.next

        while curr:
            result.append(curr.val)
            curr = curr.next

        return result
