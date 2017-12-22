from collections import defaultdict

def load_data():
    grid = defaultdict(int)

    with open("22_input.txt") as file:
        raw_data = file.read().strip().split("\n")
    height = len(raw_data)
    width = len(raw_data[0])
    for i in range(width):
        for j in range(height):
            grid[i + 1j*j] = 1 if raw_data[j][i] == "#" else 0
    pos = ((width-1)//2) + 1j*((height-1)//2)
    
    return grid, pos

"""
Note: both parts operate on a number grid where -i is considered "up". 
This is the opposite of how the complex plane is usually drawn, 
but it makes the file loading code easier.
This means that a clockwise turn and a counterclockwise turn
are accomplished by multiplying by i^1 and i^3 respectively,
rather than the usual vice versa.
"""

#part 1
grid, pos = load_data()
heading = -1j
count = 0
for _ in range(10000):
    if grid[pos]:
        heading *= 1j
    else:
        heading *= 1j**3
    grid[pos] ^= 1
    count += grid[pos]
    pos += heading

print(count)

#part 2
grid, pos = load_data()
heading = -1j
count = 0

CLEAN = 0
WEAKENED = 1
INFECTED = 2
FLAGGED = 3

grid = defaultdict(int, {p: 0 if v == 0 else INFECTED for p,v in grid.items()})

for _ in range(10000000):
    heading *= 1j**((grid[pos]-1)%4)
    grid[pos] = (grid[pos] + 1)%4
    if grid[pos] == INFECTED:
        count += 1
    pos += heading
print(count)
