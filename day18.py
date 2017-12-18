from collections import defaultdict

with open("input.txt") as file:
    program = [line.split() for line in file]

class Thread:
    def __init__(self, program, pid):
        self.program = program
        self.registers = defaultdict(int)
        self.registers["p"] = pid
        self.pc = 0
        self.queue = []
        self.buddy = None
        self.times_sent = 0
        self.last_played = None
    def get(self, x):
        return self.registers[x] if x in self.registers else int(x)
    def terminated(self):
        return not 0 <= self.pc < len(self.program)
    def blocked(self):
        return len(self.queue) == 0 and self.program[self.pc][0] == "rcv" and self.buddy
    def can_run(self):
        return not self.terminated() and not self.blocked()
    def tick(self):
        assert self.can_run()
        op, *args = self.program[self.pc]
        if op == "snd":
            if self.buddy:
                #part 2 style behavior
                self.buddy.queue.append(self.get(args[0]))
                self.times_sent += 1
            else:
                #part 1 style behavior
                self.last_played = self.get(args[0])
        elif op == "rcv":
            if self.buddy:
                #part 2 style behavior
                self.registers[args[0]] = self.queue.pop(0)
            else:
                #part 1 style behavior
                if self.get(args[0]):
                    print(self.last_played)
                    self.pc = -1
                    return
        elif op == "set":
            self.registers[args[0]] = self.get(args[1])
        elif op == "add":
            self.registers[args[0]] += self.get(args[1])
        elif op == "mul":
            self.registers[args[0]] *= self.get(args[1])
        elif op == "mod":
            self.registers[args[0]] %= self.get(args[1])
        elif op == "jgz":
            if self.get(args[0]) > 0:
                self.pc += self.get(args[1])
                return
        self.pc += 1

#part 1
t = Thread(program, 0)
while t.can_run():
    t.tick()

#part 2
threads = [Thread(program, i) for i in range(2)]
for i in range(2):
    threads[i].buddy = threads[1-i]
while True:
    candidates = [t for t in threads if t.can_run()]
    if not candidates:
        break
    candidates[0].tick()

print(threads[1].times_sent)
