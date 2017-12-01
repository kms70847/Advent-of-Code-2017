def iter_offset_pairs(seq, offset):
    for i in range(len(seq)):
        yield seq[i], seq[(i+offset)%len(seq)]

def match_sum(s, offset):
    return sum(int(a) for a,b in iter_offset_pairs(s, offset) if a==b)

with open("01_input.txt") as file:
    data = file.read().strip()

print(match_sum(data, 1))
print(match_sum(data, len(data)//2))
