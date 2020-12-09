
def solve(f):
    nums = [int(num) for num in f.splitlines()]
    
    def compute_sums(prev):
        sums = []
        for i in prev:
            for j in prev:
                sums.append(i + j)
        return sums

    for i, num in enumerate(nums[25:]):
        prev = nums[i:25+i]
        print(i)
        print(nums[i-25:i])
        sums = compute_sums(prev)
        if num not in sums:
            return num

    
def main():
    with open("input.txt") as f:
        print(solve(f.read()))


if __name__ == "__main__":
    main()
