def solve(args):
    passports = args.split("\n\n")
    valid = 0
    reqs = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    ps = []
    for passport in passports:
        fields = passport.split()
        ps.append(fields)
    
    for p in ps:
        good = True 
        for req in reqs:
            req_found = False
            for field in p:
                if req in field:
                    req_found = True
            if not req_found:
                good = False


        if good:
            valid += 1
        
    print(valid)
    
        
    
def main():
    with open("input.txt") as f:
        solve(f.read())


if __name__ == "__main__":
    main()
