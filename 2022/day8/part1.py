from aocd.models import Puzzle  # type: ignore[import]


def main() -> None:
    puzzle = Puzzle(year=2022, day=8)
    inp = puzzle.input_data
    inp = """30373
25512
65332
33549
35390"""
    grid = [[int(cell) for cell in row] for row in inp.split("\n")]
    visible_trees = set()
    for i in range(len(grid)):
        last_tree_height = -1
        for j in range(len(grid[i])):
            if grid[i][j] < last_tree_height:
                break
            if grid[i][j] > last_tree_height:
                visible_trees.add((i, j))
            last_tree_height = grid[i][j]
        last_tree_height = -1
        for j in range(len(grid[i]) - 1, -1, -1):
            if grid[i][j] < last_tree_height:
                break
            if grid[i][j] > last_tree_height:
                visible_trees.add((i, j))
            last_tree_height = grid[i][j]
    # print(visible_trees)
    # print(len(visible_trees))
    for j in range(len(grid[0])):
        last_tree_height = -1
        for i in range(len(grid)):
            if grid[i][j] < last_tree_height:
                break
            if grid[i][j] > last_tree_height:
                visible_trees.add((i, j))
            last_tree_height = grid[i][j]
        last_tree_height = -1
        for i in range(len(grid) - 1, -1, -1):
            if grid[i][j] < last_tree_height:
                break
            if grid[i][j] > last_tree_height:
                visible_trees.add((i, j))
            last_tree_height = grid[i][j]
    print(len(visible_trees))


if __name__ == "__main__":
    main()
