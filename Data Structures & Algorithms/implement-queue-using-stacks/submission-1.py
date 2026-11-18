class MyQueue:

    def __init__(self):
        self.st1=[]
        self.st2=[]
        self.q=self.st1
        

    def push(self, x: int) -> None:
        self.q=[x]+self.q

    def pop(self) -> int:
        return self.q.pop()

    def peek(self) -> int:
        return self.q[-1]

    def empty(self) -> bool:
        return self.q==[]


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()