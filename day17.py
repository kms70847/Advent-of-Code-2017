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

#part 1
buf = create_buffer(394, 2017)
print(value_after(buf, 2017))

#part 2
step = 394
idx = 0
x = None
for i in range(1, 50000001):
    if idx == 0:
        x = i
    idx = (idx + step + 1) % (i+1) 
print(x)
