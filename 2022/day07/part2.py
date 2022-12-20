from typing import TypedDict

from aocd.models import Puzzle  # type: ignore[import]

TOTAL_DRIVE_SPACE = 70000000
UNUSED_SPACE_NEEDED = 30000000


class FileTreeNode(TypedDict):
    files: list[tuple[str, int]]
    directories: dict[str, "FileTreeNode"]
    size: int


def get_folder_tree_from_path(
    current_path: list[str], file_tree: FileTreeNode
) -> FileTreeNode:
    current_folder = file_tree
    for folder_name in current_path:
        current_folder = current_folder["directories"][folder_name]
    return current_folder


def main() -> None:
    puzzle = Puzzle(year=2022, day=7)
    lines = puzzle.input_data.split("\n")

    current_path: list[str] = []
    file_tree: FileTreeNode = {"files": [], "directories": {}, "size": 0}
    folder_totals: dict[str, int] = {}

    i: int = 0
    while i < len(lines):
        cmd = lines[i][2:].split(" ")[0]
        if cmd == "cd":
            file_path = lines[i][2:].split(" ")[1]
            if file_path == "/":
                current_path = []
            elif file_path == "..":
                current_path.pop()
            else:
                current_path.append(file_path)
        elif cmd == "ls":
            while (i + 1) < len(lines) and lines[i + 1][0] != "$":
                dir_or_size: str
                file_or_folder_name: str
                dir_or_size, file_or_folder_name = lines[i + 1].split(" ")
                current_folder = get_folder_tree_from_path(current_path, file_tree)
                if dir_or_size == "dir":
                    current_folder["directories"][file_or_folder_name] = {
                        "files": [],
                        "directories": {},
                        "size": 0,
                    }
                else:
                    current_folder["files"].append(
                        (file_or_folder_name, int(dir_or_size))
                    )
                    for j in range(len(current_path) + 1):
                        folder_tree = get_folder_tree_from_path(
                            current_path[:j], file_tree
                        )
                        folder_tree["size"] += int(dir_or_size)
                        folder_totals["/".join(current_path[:j])] = folder_tree["size"]
                i += 1
        i += 1
    current_unused_space = TOTAL_DRIVE_SPACE - folder_totals[""]
    amount_to_be_freed = UNUSED_SPACE_NEEDED - current_unused_space
    print(min(v for v in folder_totals.values() if v >= amount_to_be_freed))


if __name__ == "__main__":
    main()
