import heapq

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = {}
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)
        self.edges[value] = []

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append((to_node, distance))
        self.edges[to_node].append((from_node, distance))  # якщо граф неорієнтований
        self.distances[(from_node, to_node)] = distance
        self.distances[(to_node, from_node)] = distance  # якщо граф неорієнтований

def dijkstra(graph, initial):
    visited = {initial: 0}
    path = {}

    nodes = set(graph.nodes)
    heap = [(0, initial)]
    
    while nodes and heap:
        current_distance, min_node = heapq.heappop(heap)
        
        if min_node in nodes:
            nodes.remove(min_node)
        
            for edge in graph.edges[min_node]:
                weight = edge[1]
                neighbor = edge[0]
                distance = current_distance + weight
                
                if neighbor not in visited or distance < visited[neighbor]:
                    visited[neighbor] = distance
                    heapq.heappush(heap, (distance, neighbor))
                    path[neighbor] = min_node

    return visited, path

def main():
    graph = Graph()
    
    # Додаємо вершини
    for node in 'ABCDEFG':
        graph.add_node(node)
    
    # Додаємо ребра та їх ваги
    edges = [
        ('A', 'B', 1),
        ('A', 'C', 4),
        ('B', 'C', 2),
        ('B', 'D', 5),
        ('C', 'D', 1),
        ('D', 'E', 3),
        ('E', 'F', 1),
        ('F', 'G', 2),
        ('E', 'G', 2),
    ]
    
    for edge in edges:
        graph.add_edge(*edge)
    
    # Початкова вершина
    initial = 'A'
    
    # Обчислюємо найкоротші шляхи
    distances, paths = dijkstra(graph, initial)
    
    # Виведення результатів
    print("Відстані від вершини", initial)
    for node in distances:
        print(f"До вершини {node}: {distances[node]}")

    print("\nШляхи:")
    for node in paths:
        print(f"{node}: {paths[node]}")

if __name__ == "__main__":
    main()
