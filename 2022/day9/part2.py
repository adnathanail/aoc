from aocd.models import Puzzle  # type: ignore[import]

from utils import Pos, get_head_positions


def drag_knot(leader: Pos, follower: Pos) -> Pos:
    dx, dy = leader.x - follower.x, leader.y - follower.y
    if abs(dx) == 2 and abs(dy) == 2:
        return Pos(leader.x - (dx // 2), leader.y - (dy // 2))
    elif abs(dx) == 2 or abs(dy) == 2:
        altx = 1 if dx > 0 else -1 if dx < 0 else 0
        alty = 1 if dy > 0 else -1 if dy < 0 else 0
        return Pos(follower.x + altx, follower.y + alty)
    else:
        return follower


def main() -> None:
    puzzle = Puzzle(year=2022, day=9)
    t_positions = {Pos(0, 0)}
    knot_positions = {
        "1": Pos(0, 0),
        "2": Pos(0, 0),
        "3": Pos(0, 0),
        "4": Pos(0, 0),
        "5": Pos(0, 0),
        "6": Pos(0, 0),
        "7": Pos(0, 0),
        "8": Pos(0, 0),
        "9": Pos(0, 0),
    }
    tail_path = []
    for h_pos in get_head_positions(puzzle.input_data):
        knot_positions["1"] = drag_knot(h_pos, knot_positions["1"])
        knot_positions["2"] = drag_knot(knot_positions["1"], knot_positions["2"])
        knot_positions["3"] = drag_knot(knot_positions["2"], knot_positions["3"])
        knot_positions["4"] = drag_knot(knot_positions["3"], knot_positions["4"])
        knot_positions["5"] = drag_knot(knot_positions["4"], knot_positions["5"])
        knot_positions["6"] = drag_knot(knot_positions["5"], knot_positions["6"])
        knot_positions["7"] = drag_knot(knot_positions["6"], knot_positions["7"])
        knot_positions["8"] = drag_knot(knot_positions["7"], knot_positions["8"])
        knot_positions["9"] = drag_knot(knot_positions["8"], knot_positions["9"])
        if knot_positions["9"] not in t_positions:
            tail_path.append(knot_positions["9"])
        t_positions.add(knot_positions["9"])
        # Print function for first test input
        # for i in range(4, -1, -1):
        #     for j in range(6):
        #         ij_pos = Pos(j, i)
        #         if h_pos == ij_pos:
        #             print("H", end="")
        #             continue
        #         printed = False
        #         for k in range(1, 9 + 1):
        #             if knot_positions[str(k)] == ij_pos:
        #                 print(k, end="")
        #                 printed = True
        #                 break
        #         if not printed:
        #             print(".", end="")
        #     print()
        # print()
    print(len(t_positions))


if __name__ == "__main__":
    main()
