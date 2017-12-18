STEP = 394

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def insert_after(self, value):
        x = Node(value)
        x.next = self.next
        self.next = x
    def __iter__(self):
        cur = self
        while cur is not None:
            yield cur.value
            cur = cur.next
        
def value_after(iterable, target):
    g = iter(iterable)
    for x in g:
        if x == target:
            break
    return next(g)

def create_buffer(step, rounds):
    start = cur = Node(0)
    cur.next = cur
    for i in range(1, rounds+1):
        for _ in range(step):
            cur = cur.next
        cur.insert_after(i)
        cur = cur.next
    return start

def number_following_zero(step, rounds):
    #two observations:
    #1. We can easily keep track of zero's index, and the state of the 
    #   index following it, without having to keep track of the value at any
    #   other index. So we have O(1) memory consumption.
    #2. When the buffer has a size of at least `k*step` where k >= 2, 
    #   we can skip at least k-1 intermediate insertions, which can provide
    #   substantial performance increases compared to the conventional approach,
    #   when `rounds` is much larger than `step`. 
    #   Which it happens to be for part 2 :-)
    idx = 0
    x = None
    size = 1
    while size < rounds+1:
        insertions_this_loop = (size - idx) // step
        
        if idx == 0:
            x = size
        if insertions_this_loop > 0:
            size += insertions_this_loop
            idx = (idx + (step+1)*insertions_this_loop) % size
        else:
            size += 1
            idx = (idx + step + 1)% (size)
    return x

#part 1
buf = create_buffer(STEP, 2017)
print(value_after(buf, 2017))

#part 2
print(number_following_zero(STEP, 50000000))
