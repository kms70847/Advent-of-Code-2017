def gen(seed, factor):
    current = seed
    while True:
        current = (current * factor) % 2147483647
        yield current


def similarity(iter_a, iter_b, rounds):
    mask = 2**16 - 1
    count = 0
    for i in range(rounds):
        if (next(gen_a) & mask) ^ (next(gen_b) & mask) == 0:
            count += 1
    return count

gen_a = gen(703, 16807)
gen_b = gen(516, 48271)


#part 1
print(similarity(gen_a, gen_b, 40000000))

#part 2
gen_a = (x for x in gen(703, 16807) if x%4 == 0)
gen_b = (x for x in gen(516, 48271) if x%8 == 0)
print(similarity(gen_a, gen_b, 5000000))
