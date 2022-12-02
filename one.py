import utils


def part_one():
    puzzle_input = utils.get_puzzle_input(day="one")
    return max([sum(map(int, elf.split("\n"))) for elf in puzzle_input.split("\n\n")])


def part_two():
    puzzle_input = utils.get_puzzle_input(day="one")
    return sum(sorted([sum(map(int, elf.split("\n"))) for elf in puzzle_input.split("\n\n")])[-3:])


if __name__ == "__main__":
    print(part_one())
    print(part_two())
