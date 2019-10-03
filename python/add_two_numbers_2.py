class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        dummyHead = ListNode(-1)
        t1 = l1
        t2 = l2
        curr = dummyHead

        carry = 0
        while t1 is not None or t2 is not None:
            x = 0 if t1 is None else t1.val
            y = 0 if t2 is None else t2.val

            tmp = x + y + carry
            carry = tmp / 10
            curr.next = ListNode(tmp % 10)
            curr = curr.next

            if t1 is not None:
                t1 = t1.next
            if t2 is not None:
                t2 = t2.next
        
        if carry != 0:
            curr.next = ListNode(1)

        return dummyHead.next
