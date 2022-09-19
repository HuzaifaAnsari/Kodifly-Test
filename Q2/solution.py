# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def removeNthFromEnd(self, head: [ListNode], n: int) -> [ListNode]:
        self.head=head
        self.n=n
        if n<=len(head):
            head.pop(-n)
            return head
        else:
            return print("Index Out of Range")

solv=Solution()
res=solv.removeNthFromEnd(head=[1,2,3,4],n=2)
print(res)