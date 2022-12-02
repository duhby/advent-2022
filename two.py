import utils


def part_one():
    puzzle_input = utils.get_puzzle_input(day="two")
    rpc_scores = {"X": 1, "Y": 2, "Z": 3}
    wins = ["A Y", "B Z", "C X"]
    losses = ["A Z", "B X", "C Y"]
    ties = ["A X", "B Y", "C Z"]
    score = 0
    for round_ in puzzle_input.splitlines():
        score += rpc_scores[round_.split()[-1]]
        if round_ in wins:
            score += 6
        elif round_ in losses:
            continue
        elif round_ in ties:
            score += 3
    return score


def part_two():
    puzzle_input = utils.get_puzzle_input(day="two")
    rpc_scores = {"A": 1, "B": 2, "C": 3}
    outcome_scores = {"X": 0, "Y": 3, "Z": 6}
    # Position 0 gives what you need to win
    # Position 1 gives what you need to lose
    shape_map = {"A": ["B", "C"], "B": ["C", "A"], "C": ["A", "B"]}
    score = 0
    for round_ in puzzle_input.splitlines():
        shape, outcome = round_.split()
        score += outcome_scores[outcome]
        if outcome == "X":
            score += rpc_scores[shape_map[shape][1]]
        elif outcome == "Y":
            score += rpc_scores[shape]
        elif outcome == "Z":
            score += rpc_scores[shape_map[shape][0]]
    return score


if __name__ == '__main__':
    print(part_one())
    print(part_two())
