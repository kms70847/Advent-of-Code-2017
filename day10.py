import functools

def hash_round(seq, lengths, idx=0, skip_size=0):
    seq = seq[:]
    for length in lengths:
        vals = [seq[(idx+i)%len(seq)] for i in range(length)][::-1]
        for i, val in enumerate(vals):
            seq[(idx+i)%len(seq)] = val
        idx = (idx + length + skip_size) % len(seq)
        skip_size += 1
    return seq, idx, skip_size

def knot_hash(message):
    seq = list(range(256))
    lengths = [ord(c) for c in message] + [17, 31, 73, 47, 23]
    idx = 0
    skip_size = 0
    for i in range(64):
        seq, idx, skip_size = hash_round(seq, lengths, idx, skip_size)
    blocks = [seq[i:i+16] for i in range(0, len(seq), 16)]
    multi_xor = lambda seq: functools.reduce(lambda a,b: a^b, seq, 0)
    dense_hash = list(map(multi_xor, blocks))
    result = "".join("{:0>2x}".format(x) for x in dense_hash)
    return result

with open("10_input.txt") as file:
    raw_data = file.read().strip()

#part 1
lengths = list(map(int, raw_data.split(",")))
seq = list(range(256))
seq, _, _ = hash_round(seq, lengths)
print(seq[0] * seq[1])

#part 2
print(knot_hash(raw_data))
