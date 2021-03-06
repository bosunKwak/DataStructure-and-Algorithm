import collections


class Stack:
    def __init__(self):
        self.q = collections.deque()

    #queue를 이용해 재정렬
    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self):
        return self.q.popleft()

    def top(self):
        return self.q[0]

    def empty(self):
        return len(self.q) == 0


stack = Stack()
stack.push(1)
stack.push(2)
print(stack.top())
stack.pop()
if stack.empty():
    print("empty")
else:
    print("not empty")