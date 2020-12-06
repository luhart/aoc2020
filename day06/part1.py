def solve(f):
    groups = f.split("\n\n")
    counts = 0
    for group in groups:
        group = group.strip().replace("\n", "")
        counts += len(set(group))
    print(counts)


def main():
    with open("input.txt") as f:
        solve(f.read())


if __name__ == "__main__":
    main()
