INPUT_TEST = """\
light red bags contain 1 bright white bag, 2 muted yellow bags.
dark orange bags contain 3 bright white bags, 4 muted yellow bags.
bright white bags contain 1 shiny gold bag.
muted yellow bags contain 2 shiny gold bags, 9 faded blue bags.
shiny gold bags contain 1 dark olive bag, 2 vibrant plum bags.
dark olive bags contain 3 faded blue bags, 4 dotted black bags.
vibrant plum bags contain 5 faded blue bags, 6 dotted black bags.
faded blue bags contain no other bags.
dotted black bags contain no other bags.
"""

def intable(s):
    try: 
        int(s)
        return True
    except ValueError:
        return False

def parse(rules):
    """Filter out text not necessary for each rule"""
    parsed_rules = {}
    for rule in rules:
        color = " ".join(rule.split(" ")[:2])
        holds = rule.split(" ")[4:]
        if not intable(holds[0][0]):
            parsed_rules[color] = None
            continue
        holds = [hold for hold in holds if ("bag" not in hold) and (not intable(hold))]
        holds_colors = []
        for i in range(0, len(holds), 2):
            holds_colors.append(holds[i] + " " + holds[i+1])
        parsed_rules[color] = holds_colors
    return parsed_rules

def solve(f, test=False):
    rules = []
    if test:
        rules = parse(INPUT_TEST.splitlines())
    else:
        rules = parse(f.splitlines())

    # build can_contain_gold set
    can_contain_gold = set()
    for color, holds in rules.items():
        if holds is None:
            continue
        elif "shiny gold" in holds:
            can_contain_gold.add(color)
        else:
            for nested in holds:
    return(len(can_contain_gold))

def holds_gold()

def main():
    with open("input.txt") as f:
        print(solve(f.read(), test=False))


if __name__ == "__main__":
    main()
