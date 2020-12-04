def solve(args):
    d = args.splitlines()
    m = []
    for line in d:
        m.append([char for char in line])
    
    xs = [1,3,5,7,1]
    ys = [1,1,1,1,2]

    collisions = []

    for index, x in enumerate(xs):
        x_diff = x
        y_diff = ys[index]

        x_cur = 0
        trees = 0
        for i in range(0, len(m), y_diff):
            level = m[i]
            if level[x_cur % len(level)] == "#":
                trees += 1
            x_cur += x_diff
        collisions.append(trees)
        
    print(collisions)
    mult = 1
    for item in collisions:
        mult *= item

    print(mult)
        
    
def main():
    with open("input.txt") as f:
        solve(f.read())


if __name__ == "__main__":
    main()

