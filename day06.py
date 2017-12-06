INPUT = "5	1	10	0	1	7	13	14	3	12	8	10	7	12	0	6"

def redist(bank):
    idx,amt = max(enumerate(bank), key=lambda p:(p[1],-p[0]))
    bank = list(bank)
    bank[idx] = 0
    for i in range(1,amt+1):
        bank[(idx+i)%len(bank)] += 1
    return tuple(bank)

bank = tuple(map(int, INPUT.split()))
seen = set()
seq = []
while bank not in seen:
    seen.add(bank)
    seq.append(bank)
    bank = redist(bank)

print(len(seen))
print(len(seq) - seq.index(bank))
