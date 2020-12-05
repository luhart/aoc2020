import sys 

def solve(args):
    passports = args.split("\n\n")
    num_valid = 0
    reqs = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    ps = []
    for passport in passports:
        fields = passport.split()
        ps.append(fields)
    ps = has_required_fields(ps)
    
    for p in ps:
        valid = True
        for field in p:
            pair = field.split(":")
            att = pair[0]
            val = pair[1]
            
            if att == "byr":
                val = int(val)
                if val >= 1920 and val <= 2002:
                    continue
                else: 
                    valid = False
                    break
            if att == "iyr":
                val = int(val)
                if val >= 2010 and val <= 2020:
                    continue
                else:
                    valid = False
                    break
            if att == "eyr":
                val = int(val)
                if val >= 2020 and val <= 2030:
                    continue
                else:
                    valid = False
                    break
            if att == "hgt":
                if "cm" in val:
                    val = int(val.split("cm")[0])
                    if val >= 150 and val <= 193:
                        continue
                    else:
                        valid = False
                        break
                elif "in" in val:
                    val = int(val.split("in")[0])
                    if val >= 59 and val <= 76:
                        continue
                    else:
                        valid = False
                        break
                else:
                    valid = False
                    break
            if att == "hcl":
                if val[0] == "#" and len(val) == 7:
                    continue
                else: 
                    valid = False
                    break
            if att == "ecl":
                colors = ["amb", "blu", "brn", "gry", "grn", "hzl", "oth"]
                if val in colors:
                    continue
                else:
                    valid = False
                    break
            if att == "pid":
                if len(val) == 9:
                    try:
                        nums = int(val[1:])
                    except ValueError:
                        valid = False
                        break
                    finally:
                        continue
                else:
                    valid = False
                    break
        if valid:
            num_valid += 1
    print(num_valid)



def has_required_fields(passports):
    reqs = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"]
    valid = []
    
    for p in passports:
        good = True 
        for req in reqs:
            req_found = False
            for field in p:
                if req in field:
                    req_found = True
            if not req_found:
                good = False


        if good:
            valid.append(p)
        
    return valid
    
def main():
    with open("input.txt") as f:
        solve(f.read())


if __name__ == "__main__":
    main()

