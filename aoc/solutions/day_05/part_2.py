def check(update, rules):
    # Check every pair and ensure no rules are broken
    for i, left in enumerate(update[:-1]):
        for right in update[i + 1 :]:
            if (right, left) in rules:
                return False
    return True


def fix(update: list[int], rules):
    # Step through updates. If any latter values should precede current position, move them to current position and restart.
    pos = 0
    while pos < len(update):
        left = update[pos]
        for j, right in enumerate(update[pos + 1 :]):
            i = pos + j + 1
            if (right, left) in rules:
                update.insert(pos, update.pop(i))
                break
        else:
            pos += 1

    return update


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
        if not check(update, rules):
            update = fix(update, rules)
            total += update[len(update) // 2]
    return total
