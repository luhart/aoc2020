def solve(f):
    groups = f.split("\n\n")
    counts = 0

    def get_shared_yeses(people):
        return set.intersection(*map(set, people))

    for group in groups:
        people = group.split("\n")
        shared_yeses = get_shared_yeses(people)
        counts += len(shared_yeses)

    print(counts)


def main():
    with open("input.txt") as f:
        solve(f.read())


if __name__ == "__main__":
    main()

