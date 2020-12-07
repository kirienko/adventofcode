import networkx as nx

with open('./data/day_07.txt') as fd:
    data = fd.read().split('\n')


# Parse rules into a DAG
data = dict(x.split(' bags contain ') for x in data)
rules = dict()
for k, v in data.items():
    rules[k] = dict()
    for rule in v.split(', '):
        if rule == 'no other bags.':
            continue
        else:
            num, color = rule.split(' ', 1)
            color, _ = color.rsplit(' ', 1)
            rules[k].update({color: int(num)})
G = nx.DiGraph(rules)

mine_bag = "shiny gold"

# Part 1: breadth first search of all predecessors:
T = nx.bfs_tree(G.reverse(), source=mine_bag)
print(f"Answer 1: {len(T.nodes) - 1}")

# Part 2: breadth first search of all successors
nx.set_node_attributes(G, 0, name='bags')
G.nodes[mine_bag]['bags'] = 1

# Select a subset of my bag's content
T = nx.bfs_tree(G, source=mine_bag)
# create a subgraph from these nodes
N = G.subgraph(list(T))

# all paths from the source to every node
for n in N.nodes:
    for path in nx.all_simple_edge_paths(N, source=mine_bag, target=n):
        path_w = 1
        for f, t in path:
            path_w *= rules[f][t]
        G.nodes[n]['bags'] += path_w
    # print(f"Bags in [{n}] = {G.nodes[n]['bags']}")

print(f"Answer 2: {sum(N.nodes[n]['bags'] for n in N.nodes)-1}")
nodes = list(T)[1:]
