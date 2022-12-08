import networkx as nx


def get_file_tree(text: str) -> nx.DiGraph:
    """ Parse input text and create a tree (DAG) """
    G = nx.DiGraph()

    cur_dir = '/'
    text = text.strip().replace('$ cd /', '')

    for line in text.strip().split('\n'):
        if len(line.split()) == 3:
            a, b, c = line.split()
            if b == 'cd' and c != '..':
                next_node = f"{cur_dir}/{c}" if cur_dir != '/' else f"/{c}"
                G.add_edge(cur_dir, next_node)
                cur_dir = next_node
            else:
                cur_dir = next(G.predecessors(cur_dir))
        else:
            a, b = line.split()
            next_node = f"{cur_dir}/{b}" if cur_dir != '/' else f"/{b}"
            if a == 'dir':
                G.add_edge(cur_dir, next_node)
            elif a == '$':
                continue
            else:
                G.add_edge(cur_dir, next_node, size=int(a))
    return G


def full_dir_size(G: nx.DiGraph, dn: str) -> int:
    """ Size of the "directory" `dn` """
    return nx.tree.branching_weight(G.subgraph(nx.dfs_tree(G, source=dn).nodes), attr='size', default=0)


def task1(text: str) -> int:
    G = get_file_tree(text)
    result = 0
    for node in G.nodes:
        size = full_dir_size(G, node)
        if size <= 100000:
            result += size
    return result


def task2(text: str) -> int:
    G = get_file_tree(text)

    dirs = [full_dir_size(G, node) for node in G.nodes]

    disk_size = 70000000
    needed = 30000000
    root = max(dirs)

    for d in sorted(dirs):
        if disk_size - root + d > needed:
            return d


if __name__ == "__main__":
    with open('data/day_07.txt') as fd:
        data = fd.read()

    print(task1(data))
    print(task2(data))
