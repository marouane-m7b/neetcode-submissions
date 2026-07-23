class ListNode:
    def __init__(self, val,prev=None,next=None):
        self.val = val
        self.prev = prev
        self.next = next


class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = ListNode(homepage)
        

    def visit(self, url: str) -> None:
        self.cur.next = ListNode(url)
        self.cur.next.prev = self.cur
        self.cur = self.cur.next

        

    def back(self, steps: int) -> str:
        i = 0
        while i < steps:
            if self.cur.prev:
                self.cur = self.cur.prev
            i+=1

        return self.cur.val
        

    def forward(self, steps: int) -> str:
        i = 0
        while i < steps:
            if self.cur.next:
                self.cur = self.cur.next
            i+=1

        return self.cur.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)