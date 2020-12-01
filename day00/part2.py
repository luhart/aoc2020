def solve(args):
    numbers = set(map(int, args.splitlines()))

    for first in numbers:
        for second in numbers:
            for third in numbers:
                if first + second + third == 2020:
                    print("found")
                    return first * second * third
    return "not found"


def main():
    with open("input.txt") as f:
        print(solve(f.read()))


if __name__ == "__main__":
    main()
