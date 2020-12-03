def solve(args):
    rows = args.splitlines()
    valid = 0
    for line in rows:
        nums, letter, pw = line.split(" ")
        nums = nums.split("-")
        lower = int(nums[0])
        upper = int(nums[1])
        letter = letter[0]

        count = 0
        for char in pw:
            if char == letter:
                count += 1
        if count >= lower and count <= upper:
            valid += 1
                                                              
    print(valid)
    



    
def main():
    with open("input.txt") as f:
        print(solve(f.read()))


if __name__ == "__main__":
    main()
