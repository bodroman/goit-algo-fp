import uuid
import networkx as nx
import matplotlib.pyplot as plt
from collections import deque

class Node:
    def __init__(self, key, color="skyblue"):
        self.left = None
        self.right = None
        self.val = key
        self.color = color
        self.id = str(uuid.uuid4())

def build_heap_tree(heap, index=0):
    if index >= len(heap):
        return None
    
    node = Node(heap[index])
    node.left = build_heap_tree(heap, 2 * index + 1)
    node.right = build_heap_tree(heap, 2 * index + 2)
    return node

def add_edges(graph, node, pos, x=0, y=0, layer=1):
    if node is not None:
        graph.add_node(node.id, color=node.color, label=node.val)
        if node.left:
            graph.add_edge(node.id, node.left.id)
            l = x - 1 / 2 ** layer
            pos[node.left.id] = (l, y - 1)
            l = add_edges(graph, node.left, pos, x=l, y=y - 1, layer=layer + 1)
        if node.right:
            graph.add_edge(node.id, node.right.id)
            r = x + 1 / 2 ** layer
            pos[node.right.id] = (r, y - 1)
            r = add_edges(graph, node.right, pos, x=r, y=y - 1, layer=layer + 1)
    return graph

def draw_tree(tree_root, visited_nodes=None, filename=None):
    tree = nx.DiGraph()
    pos = {tree_root.id: (0, 0)}
    tree = add_edges(tree, tree_root, pos)

    colors = [node[1]['color'] for node in tree.nodes(data=True)]
    labels = {node[0]: node[1]['label'] for node in tree.nodes(data=True)}

    plt.figure(figsize=(8, 5))
    nx.draw(tree, pos=pos, labels=labels, arrows=False, node_size=2500, node_color=colors)

    if visited_nodes:
        for node in visited_nodes:
            nx.draw_networkx_nodes(tree, pos, nodelist=[node.id], node_color=node.color)

    if filename:
        plt.savefig(filename)
    plt.show()

def rgb_to_hex(rgb):
    return '#{:02x}{:02x}{:02x}'.format(int(rgb[0]*255), int(rgb[1]*255), int(rgb[2]*255))

def get_color_gradient(n):
    return [(i/n, 0, 1-i/n) for i in range(n)]

def bfs(tree_root):
    queue = deque([tree_root])
    visited = []
    colors = get_color_gradient(len(heap))

    i = 0
    while queue:
        node = queue.popleft()
        node.color = rgb_to_hex(colors[i])
        visited.append(node)
        i += 1
        draw_tree(tree_root, visited_nodes=visited, filename=f'bfs_step_{i}.png')
        if node.left:
            queue.append(node.left)
        if node.right:
            queue.append(node.right)

def dfs(tree_root):
    stack = [tree_root]
    visited = []
    colors = get_color_gradient(len(heap))

    i = 0
    while stack:
        node = stack.pop()
        node.color = rgb_to_hex(colors[i])
        visited.append(node)
        i += 1
        draw_tree(tree_root, visited_nodes=visited, filename=f'dfs_step_{i}.png')
        if node.right:
            stack.append(node.right)
        if node.left:
            stack.append(node.left)

# Приклад використання
heap = [10, 5, 6, 2, 4, 3, 1]  # Список, що представляє бінарну купу
root = build_heap_tree(heap)

# Відображення обходів
bfs(root)  # Обхід в ширину
dfs(root)  # Обхід в глибину
