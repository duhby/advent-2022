import utils


def part_one():
    puzzle_input = utils.get_puzzle_input(day="three")
    priorities = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    total = 0
    for sack in puzzle_input.splitlines():
        middle = len(sack) // 2
        sack1, sack2 = sack[:middle], sack[middle:]
        common = ''.join(set(sack1).intersection(sack2))
        total += priorities.index(common) + 1
    return total


def part_two():
    puzzle_input = utils.get_puzzle_input(day="three")
    priorities = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
    total = 0
    sacks = puzzle_input.splitlines()
    sack_groups = [sacks[i:i+3] for i in range(0, len(sacks), 3)]
    for group in sack_groups:
        common = ''.join(set(group[0]).intersection(group[1], group[2]))
        total += priorities.index(common) + 1
    return total


if __name__ == "__main__":
    print(part_one())
    print(part_two())
