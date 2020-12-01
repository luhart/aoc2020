def solve(args):
    numbers = set(map(int, args.splitlines()))

    for first in numbers:
        for second in numbers:
            if first + second == 2020:
                return first * second
    return "not found"


def main():
    with open("input.txt") as f:
        print(solve(f.read()))


if __name__ == "__main__":
    main()
