import heapq

class PriorityQueue:
    def __init__(self):
        self.elements = []

    def is_empty(self):
        return not self.elements

    def put(self, item, priority):
        heapq.heappush(self.elements, (priority, item))

    def get(self):
        return heapq.heappop(self.elements)[1]

def a_star(start, goal, graph, h):
    distance = {}
    path = {}
    
    q = PriorityQueue()
    q.put(start,0)
    distance[start] = 0
    path[start] = None
    expanded_list = []

    while not q.is_empty():
        current = q.get()
        expanded_list.append(current)

        if current == goal:
            break 

        for neighbor, cost in graph[current]:
            g_cost = distance[current] + cost
            if neighbor not in distance or g_cost < distance[neighbor]:
                distance[neighbor] = g_cost
                f_cost = g_cost + h[neighbor]
                q.put(neighbor, f_cost)
                path[neighbor] = current

    optimal_path = []
    node = goal
    while node is not None:
        optimal_path.append(node)
        node = path[node]
    optimal_path.reverse()
    
    return optimal_path, distance[goal], expanded_list

graph = {}
h = {}

file1 = open("D:\Ai\Astar\input.txt", "r")
lines = file1.readlines()

for line in lines:
    parts = line.strip().split()
    if len(parts) >= 2:
            
        node = parts[0]
        heuristic_value = int(parts[1])
        h[node] = heuristic_value
         
        connections = parts[2:]
        for i in range(0, len(connections), 2):
            neighbor = connections[i]
            cost = int(connections[i + 1])
            if node not in graph:
                graph[node] = []
            graph[node].append((neighbor, cost))

    
start_node = input("Start node: ")
goal_node = input("Destination: ")

optimal_path, total_distance, expanded_list = a_star(start_node, goal_node, graph,h)

if optimal_path:
    print("Path:", end=" ")
    for i in range(len(optimal_path)):
        if i == len(optimal_path) - 1:  
            print(optimal_path[i])
        else:
            print(optimal_path[i], "->", end=" ")

    print("Total distance:", total_distance, "km")
else:
    print("NO PATH FOUND")