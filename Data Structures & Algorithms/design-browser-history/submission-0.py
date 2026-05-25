class LinkedListNode:
    def __init__(self, url):
        self.next = None
        self.prev = None
        self.url = url

class BrowserHistory:

    def __init__(self, homepage: str):
        self.head = LinkedListNode(homepage)
    
        self.history_log = 1
        self.curr_page_idx = 0
        self.curr_page = self.head

    def visit(self, url: str) -> None:
        newNode = LinkedListNode(url)
        self.curr_page.next = newNode
        newNode.prev = self.curr_page

        self.curr_page = newNode
        self.curr_page_idx += 1
        self.history_log = self.curr_page_idx + 1

    def back(self, steps: int) -> str:
        max_possible_steps = min(self.curr_page_idx, steps)
        for i in range(max_possible_steps):
            self.curr_page = self.curr_page.prev
            self.curr_page_idx -= 1
        return self.curr_page.url

    def forward(self, steps: int) -> str:
        max_possible_steps = min(self.history_log - self.curr_page_idx - 1, steps)
        for i in range(max_possible_steps):
            self.curr_page = self.curr_page.next
            self.curr_page_idx += 1
        return self.curr_page.url


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)