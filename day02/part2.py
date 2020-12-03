def solve(args):
    rows = args.splitlines()
    valid = 0
    for line in rows:
        nums, letter, pw = line.split(" ")
        nums = nums.split("-")
        first = int(nums[0])
        second = int(nums[1])
        letter = letter[0]

        if (pw[first-1]== letter and pw[second-1] != letter) or (pw[first-1] != letter and pw[second-1] == letter):
            valid += 1

    print(valid)
    
def main():
    with open("input.txt") as f:
        print(solve(f.read()))


if __name__ == "__main__":
    main()
