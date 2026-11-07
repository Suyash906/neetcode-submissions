class MinStack:

    def __init__(self):
        self.main_stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.main_stack.append(val)
        temp_stack = []
        while self.min_stack and self.min_stack[-1] < val:
            temp_stack.append(self.min_stack.pop())
        self.min_stack.append(val)
        while temp_stack:
            self.min_stack.append(temp_stack.pop())


    def pop(self) -> None:
        if self.main_stack:
            val = self.main_stack.pop()
            temp_stack = []
            while self.min_stack and self.min_stack[-1] < val:
                temp_stack.append(self.min_stack.pop())
            self.min_stack.pop()
            while temp_stack:
                self.min_stack.append(temp_stack.pop())
        

    def top(self) -> int:
        return self.main_stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
        
