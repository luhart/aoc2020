import sys

def solve(f):
    instructions = f.splitlines()
    nops_and_jmps = [(index, inst) for index, inst in enumerate(instructions) if "".join(inst[0:3]) in ["nop", "jmp"]]
    terminate = False
    for test_change in nops_and_jmps:
        change_index, _ = test_change
        accumulator = 0
        cur = 0
        visited = set()
        while True:
            if cur == len(instructions) - 1:
                terminate = True
            inst, val = instructions[cur].split(" ")
            
            if cur in visited:
                break
            else:
                visited.add(cur)

            if cur == change_index:
                if inst == "nop":
                    inst = "jmp"
                elif inst == "jmp":
                    inst = "nop"
            if inst == "nop":
                cur += 1
                continue
            elif inst == "acc":
                accumulator += int("".join(val))
                cur += 1
            elif inst == "jmp":
                cur = (cur + int("".join(val))) % len(instructions)
            
            if terminate:
                return accumulator

            
         
test = """\
nop +0
acc +1
jmp +4
acc +3
jmp -3
acc -99
acc +1
jmp -4
acc +6"""


    
def main():
    

    with open("input.txt") as f:
        print(solve(f.read()))


if __name__ == "__main__":
    main()
