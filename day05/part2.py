def solve(args):
    seats = args.splitlines()
    ids = []
    for seat in seats:
        seat = seat.replace("F", '0').replace("B", '1').replace("L", '0').replace("R", '1')
        ids.append(int(seat, 2))
    
    for i in range(1024):
        if i not in ids:
            if (i + 1 in ids) and (i - 1 in ids):
                print(i)

    
def main():
    with open("input.txt") as f:
        solve(f.read())


if __name__ == "__main__":
    main()

