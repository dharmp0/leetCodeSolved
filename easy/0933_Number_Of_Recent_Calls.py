from collections import deque
class RecentCounter:

    def __init__(self):
        
        self.counter = deque()

    def ping(self, t: int) -> int:
        
        self.counter.append(t)

        while self.counter[0] < t - 3000:
            self.counter.popleft()

        

        return len(self.counter)
