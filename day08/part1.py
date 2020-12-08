def solve(f):
    instructions = f.splitlines()
    accumulator = 0
    cur = 0

    visited = set()

    while True:
        if cur in visited:
            return accumulator
        else:
            visited.add(cur)

        inst, val = instructions[cur].split(" ")
        if inst == "nop":
            cur += 1
            continue
        elif inst == "acc":
            accumulator += int("".join(val))
            cur += 1
        elif inst == "jmp":
            cur = (cur + int("".join(val))) % len(instructions)

            
         
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
