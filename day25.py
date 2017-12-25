from collections import defaultdict
import re

STATE_PATTERN = r"""In state (.):
  If the current value is 0:
    - Write the value (\d+)\.
    - Move one slot to the (.*?)\.
    - Continue with state (.)\.
  If the current value is 1:
    - Write the value (\d+)\.
    - Move one slot to the (.*?)\.
    - Continue with state (.)\."""

with open("25_input.txt") as file:
    raw_data = file.read()

raw_header, *raw_states = raw_data.split("\n\n")

m = re.match(r"Begin in state (.)\.\nPerform a diagnostic checksum after (\d+) steps.", raw_header)
starting_state, num_steps = m.groups()
num_steps = int(num_steps)

states = {}
for raw_state in raw_states:
    m = re.match(STATE_PATTERN, raw_state)
    state_name, write_when_0, move_when_0, next_state_when_0, write_when_1, move_when_1, next_state_when_1 = m.groups()
    states[m.group(1)] = [
        {
            "write": int(m.group(2)),
            "move": 1 if m.group(3) == "right" else  -1,
            "next": m.group(4)
        },
        {
            "write": int(m.group(5)),
            "move": 1 if m.group(6) == "right" else -1,
            "next": m.group(7)
        },
    ]

tape = defaultdict(int)
cursor = 0
cur_state = states[starting_state]
for i in range(num_steps):
    x = cur_state[tape[cursor]]
    tape[cursor] = x["write"]
    cursor += x["move"]
    cur_state = states[x["next"]]

print(sum(tape.values()))
