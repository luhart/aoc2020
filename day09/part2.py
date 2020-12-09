
def compute_sums(prev):
    return [x + y for x in prev for y in prev]


def find_invalid(nums):
    for i, num in enumerate(nums[25:]):
        prev = nums[i:25+i]
        sums = compute_sums(prev)
        if num not in sums:
            return num


def solve(f):
    nums = [int(num) for num in f.splitlines()]
    invalid = find_invalid(nums)
    
    for i in range(len(nums)):
        for j in range(i+2, len(nums)):
            subset = nums[i:j]
            if sum(subset) == invalid:
                return min(subset) + max(subset)

    
def main():
    with open("input.txt") as f:
        print(solve(f.read()))


if __name__ == "__main__":
    main()
