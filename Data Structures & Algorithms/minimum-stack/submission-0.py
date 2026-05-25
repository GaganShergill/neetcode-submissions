class MinStack:

    def __init__(self):
        self.arr = []
        self.min_e = []

    def push(self, val: int) -> None:
        self.arr.append(val)
        if self.min_e:
            self.min_e.append(min(val, self.min_e[-1]))
        else:
            self.min_e.append(val)
        return

    def pop(self) -> None:
        self.arr.pop()
        self.min_e.pop()
        return

    def top(self) -> int:
        return self.arr[-1]

    def getMin(self) -> int:
        return self.min_e[-1]

        
