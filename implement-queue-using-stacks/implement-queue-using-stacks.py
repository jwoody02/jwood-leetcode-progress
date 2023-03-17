class MyQueue:

    def __init__(self):
        self._queue = []
        self._front_of_queue = 0
    def push(self, x: int) -> None:
        _tmp_queue = [0 for _ in range(len(self._queue) + 1)]
        for i, item in enumerate(self._queue):
            _tmp_queue[i] = self._queue[i]
        _tmp_queue[len(self._queue)] = x
        self._queue = _tmp_queue

    def pop(self) -> int:
        _tmp = self._queue[0]
        del self._queue[0]
        return _tmp

    def peek(self) -> int:
        return self._queue[0]

    def empty(self) -> bool:
        return len(self._queue) == 0


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()