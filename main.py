class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Box:
    def __init__(self, head = None):
        self.head = head

    def contains(self, cat):
        lastbox = self.head
        while lastbox:
            if cat == lastbox.val:
                return True
            else:
                lastbox = lastbox.next
            return False




