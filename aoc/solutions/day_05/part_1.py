def check(update, rules):
    # Check every pair and ensure no rules are broken
    for i, left in enumerate(update[:-1]):
        for right in update[i + 1:]:
            if (right, left) in rules:
                return False
    return True

def solution(path):
    with open(path) as f:
        data = f.read()
    rules_data, updates_data = data.split("\n\n")

    rules = set()
    for row in rules_data.split():
        left, right = map(int, row.split("|"))
        rules.add((left, right))

    updates = [list(map(int, row.strip().split(","))) for row in updates_data.split()]
    total = 0
    for update in updates:
        if check(update, rules):
            total += update[len(update) // 2]
    return total