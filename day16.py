import re
from collections import defaultdict

"""
So the intended solution is probably to analyze a couple rounds of data,
and see if the pattern eventually repeats, and then only do `1000000000%period`
rounds of calculations. But this is unsatisfying, since it only works on inputs
that have been specially prepared to loop quickly.

So here's an implementation that works on arbitrary inputs without assuming
they loop at all. On average, it calculates log(N,2)*2 rounds, which
should leave plenty of stack space for N = one billion.

The whole concept depends on two principles:
1. Swap moves don't depend on non-swap moves, and vice versa. For example,
   `s1,x3/4,pe/b` has the same outcome as `s1,pe/b,x3/4` and `pe/b,s1,x3/4`
2a. Given a program, and a move sequence containing only non-swap moves,
    and the program after those moves have been applied to it N times,
    you can find the program state after N*2 rounds in constant time.
2b. Same as 2b, but for "only swap moves" instead of "only non-swap moves".

So we create two specialized fast round calculators for swap moves and 
non-swap moves, then combine them at the end for a single generalized
fast round calculator.
""" 

def separate(iterable, predicate):
    results = [[],[]]
    for item in iterable:
        results[predicate(item)].append(item)
    return results

def round(seq, moves):
    seq = seq[:]
    for move in moves:    
        if move.startswith("s"):
            amt = int(move[1:])
            for i in range(amt):
                seq.insert(0, seq.pop())
        elif move.startswith("x"):
            a,b = map(int, move[1:].split("/"))
            seq[a], seq[b] = seq[b], seq[a]
        elif move.startswith("p"):
            a,b = move[1:].split("/")
            seq = [{a:b,b:a}.get(x,x) for x in seq]
        else:
            raise Exception("Unknown move {}".format(move))
    return seq

def create_specialized_fast_round(lerp_func, final_calc_func):
    def specialized_fast_round(seq, moves, num_rounds):
        if num_rounds == 0:
            return seq
        if num_rounds % 2 == 1:
            seq = round(seq, moves)
            return specialized_fast_round(seq, moves, num_rounds-1)
        midpoint = specialized_fast_round(seq, moves, num_rounds//2)
        lerp = lerp_func(seq, midpoint)
        return final_calc_func(lerp, midpoint)
    return specialized_fast_round

def rounds(seq, moves, num_rounds):
    fast_index_rounds = create_specialized_fast_round(
        lambda a,b: [a.index(x) for x in b],
        lambda lerp, midpoint: [midpoint[idx] for idx in lerp]
    )

    fast_swap_rounds = create_specialized_fast_round(
        lambda a,b: {x:y for x,y in zip(b,a)},
        lambda lerp, midpoint: [lerp[x] for x in midpoint]
    )

    index_moves, swap_moves = separate(moves, lambda move: move.startswith("p"))
    seq = fast_index_rounds(seq, index_moves, num_rounds)
    seq = fast_swap_rounds(seq, swap_moves, num_rounds)
    return seq

seq = [chr(i+ord('a')) for i in range(16)]
with open("16_input.txt") as file:
    moves = file.read().strip().split(",")

print("".join(rounds(seq, moves, 1)))
print("".join(rounds(seq, moves, 1000000000)))
