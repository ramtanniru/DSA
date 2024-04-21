class MinStack:

    def __init__(self):
        self.stk = []
        self.minstk = []
    def push(self, val: int) -> None:
        self.stk.append(val)
        if self.minstk:
            self.minstk.append(min(val,self.minstk[-1]))
        else:
            self.minstk.append(val)
    def pop(self) -> None:
        self.stk.pop(-1)
        self.minstk.pop(-1)
    def top(self) -> int:
        return self.stk[-1]

    def getMin(self) -> int:
        return self.minstk[-1]