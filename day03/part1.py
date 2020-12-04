def solve(args):
    d = args.splitlines()
    m = []
    for line in d:
        m.append([char for char in line])
    
    x_diff = 3
    y_diff = 1
    x_cur = 0
    trees = 0
    for i in range(0, len(m), y_diff):
        level = m[i]
        if level[x_cur % len(level)] == "#":
            trees += 1
        x_cur += x_diff

    print(trees)
        
    
def main():
    with open("input.txt") as f:
        solve(f.read())


if __name__ == "__main__":
    main()
