import math
import itertools

def coordinate(value):
    """finds the coordinate of the square with the given value. Positive X and Y directions are right and down respectively"""
    
    #observation: the values at (0,0), (1,1), (2,2) are 1, 9, 25.
    #So the value at (x,x) is (x*2+1)^2, for any non-negative integer x.
    #we can use this information to find the "ring" that any value lays on: just find the smallest odd square that is larger than or equal to the value.

    #find the smallest square G.T.E. the value.
    smallest_root = int(math.sqrt(value))
    if smallest_root ** 2 != value:
        smallest_root += 1

    #find the smallest odd square.
    smallest_odd_root = smallest_root + (1 if smallest_root % 2 == 0 else 0)

    ring = (smallest_odd_root - 1) // 2
    
    #once we know the ring, we can find the coordinate of the value by walking no more than one loop clockwise around the origin.
    value_at_corner = smallest_odd_root**2
    side_length = smallest_odd_root - 1 #not to be confused with the width of the entire ring, which is one larger than this
    delta = value_at_corner - value

    x,y = ring, ring
    if delta <= side_length:          #case 1: value is on bottom edge of the ring
        x -= delta
    elif delta < side_length * 2:     #case 2: value is on left edge of the ring
        x -= side_length
        y -= delta % side_length
    elif delta < side_length * 3:     #case 3: value is on top edge of the ring
        x -= side_length
        y -= side_length
        x += delta % side_length
    else:                             #case 4: value is on right edge of the ring
        y -= side_length
        y += delta % side_length
    return x,y

#part 1
target = 265149
x,y = coordinate(target)
print(abs(x) + abs(y))

#part 2
grid = {(0,0): 1}
deltas = [(x,y) for x in range(-1, 2) for y in range(-1, 2) if (x,y) != (0,0)]
for i in itertools.count(2):
    x,y = coordinate(i)
    value = 0
    for dx, dy in deltas:
        value += grid.get((x+dx, y+dy), 0)
    grid[x,y] = value
    if value > target: break
print(value)
