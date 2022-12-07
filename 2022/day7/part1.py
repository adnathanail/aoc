from aocd.models import Puzzle

puzzle = Puzzle(year=2022, day=7)

inp = """$ cd /
$ ls
dir a
14848514 b.txt
8504156 c.dat
dir d
$ cd a
$ ls
dir e
29116 f
2557 g
62596 h.lst
$ cd e
$ ls
584 i
$ cd ..
$ cd ..
$ cd d
$ ls
4060174 j
8033020 d.log
5626152 d.ext
7214296 k"""

inp = puzzle.input_data

lines = inp.split("\n")


def get_folder_tree_from_path(current_path, file_tree):
    current_folder = file_tree
    for folder_name in current_path:
        current_folder = current_folder[folder_name]
    return current_folder


def main():
    current_path = []
    file_tree = {"__files__": [], "__size__": 0}
    folder_totals = {}
    i = 0
    while i < len(lines):
        if lines[i][0] == "$":
            cmd = lines[i][2:].split(" ")[0]
            if cmd == "cd":
                file_path = lines[i][2:].split(" ")[1]
                if file_path == "/":
                    current_path = []
                elif file_path == "..":
                    current_path.pop()
                else:
                    current_path.append(file_path)
                # print(current_path)
            elif cmd == "ls":
                while (i + 1) < len(lines) and lines[i + 1][0] != "$":
                    dir_or_size, file_or_folder_name = lines[i + 1].split(" ")
                    # print(dir_or_size, file_or_folder_name)
                    current_folder = get_folder_tree_from_path(current_path, file_tree)
                    if dir_or_size == "dir":
                        current_folder[file_or_folder_name] = {"__files__": [], "__size__": 0}
                    else:
                        current_folder["__files__"].append([file_or_folder_name, int(dir_or_size)])
                        for j in range(len(current_path) + 1):
                            # print(current_path[:j])
                            folder_tree = get_folder_tree_from_path(current_path[:j], file_tree)
                            folder_tree["__size__"] += int(dir_or_size)
                            folder_totals["/".join(current_path[:j])] = folder_tree["__size__"]
                    i += 1
                # print(file_tree)
            else:
                raise Exception("Panic!")
        else:
            raise Exception("Panic!")
        i += 1
    print(file_tree)
    print(folder_totals)
    print(sum(v for v in folder_totals.values() if v <= 100000))


if __name__ == "__main__":
    main()
