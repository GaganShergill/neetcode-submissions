class LinkedListNode:
    def __init__(self, url, prev=None, next=None):
        self.next = next
        self.prev = prev
        self.url = url

class BrowserHistory:

    def __init__(self, homepage: str):
        self.cur = LinkedListNode(homepage)

    def visit(self, url: str) -> None:
        self.cur.next = LinkedListNode(url, self.cur)
        self.cur = self.cur.next

    def back(self, steps: int) -> str:
        while self.cur.prev and steps > 0:
            self.cur = self.cur.prev
            steps -= 1
        return self.cur.url

    def forward(self, steps: int) -> str:
        while self.cur.next and steps > 0:
            self.cur = self.cur.next
            steps -= 1
        return self.cur.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)