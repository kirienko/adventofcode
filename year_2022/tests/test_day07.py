from networkx import is_tree

from year_2022.day_07 import full_dir_size, get_file_tree, task1, task2

test_data = """
$ cd /
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
7214296 k
"""

G = get_file_tree(test_data)


def test_full_dir_size():
    assert full_dir_size(G, '/') == 48381165
    assert full_dir_size(G, '/d') == 24933642
    assert full_dir_size(G, '/a') == 94853
    assert full_dir_size(G, '/a/e') == 584


def test_is_tree():
    assert is_tree(G)


def test_task1(sc=test_data):
    expected = 95437
    assert task1(sc) == expected


def test_task2(sc=test_data):
    expected = 24933642
    assert task2(sc) == expected
