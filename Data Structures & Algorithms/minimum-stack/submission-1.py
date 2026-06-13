class MinStack:

    def __init__(self):
        self.st = []
        self.min = []

    def push(self, val: int) -> None:
        self.st.append(val)
        if len(self.min) == 0:
            self.min.append(val)
            return
        if self.min[-1] > val:
            print(val)
            self.min.append(val)
        elif self.min[-1] < val:
            return
        else:
            self.min.append(val)

    def pop(self) -> None:
        if not self.st:
            return
        if self.st[-1] == self.min[-1]:
            self.st.pop()
            self.min.pop()
        else:
            self.st.pop()

    def top(self) -> int:
        return self.st[-1]

    def getMin(self) -> int:
        return self.min[-1]
