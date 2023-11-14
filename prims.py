import tkinter as tk
import heapq

def prim(graph, start):
    mst = []
    visited = set()
    queue = [(0, start)]

    while queue:
        weight, node = heapq.heappop(queue)
        if node in visited:
            continue

        mst.append((node, weight))
        visited.add(node)

        for neighbor, neighbor_weight in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(queue, (neighbor_weight, neighbor))

    return mst

def get_input():
    num_buildings = int(entry_buildings.get())
    distances = []

    for i in range(num_buildings):
        row = []
        for j in range(num_buildings):
            if i == j:
                distance = 0
            else:
                distance = int(entry_distances[i][j].get())
            row.append(distance)
        distances.append(row)

    return num_buildings, distances

def calculate_mst():
    num_buildings, distances = get_input()
    graph = {i: {} for i in range(num_buildings)}

    for i in range(num_buildings):
        for j in range(num_buildings):
            if i != j:
                graph[i][j] = distances[i][j]
                graph[j][i] = distances[i][j]

    start = int(entry_start.get())
    mst = prim(graph, start)

    output_label.config(text="MST: " + str(mst))

root = tk.Tk()
root.title("Prim's Algorithm")

label_buildings = tk.Label(root, text="Number of buildings:")
label_buildings.pack()

entry_buildings = tk.Entry(root)
entry_buildings.pack()

label_distances = tk.Label(root, text="Distances:")
label_distances.pack()

entry_distances = [[tk.Entry(root) for _ in range(num_buildings)] for _ in range(num_buildings)]
for i in range(num_buildings):
    for j in range(num_buildings):
        entry_distances[i][j].pack()

label_start = tk.Label(root, text="Starting building:")
label_start.pack()

entry_start = tk.Entry(root)
entry_start.pack()

button_calculate = tk.Button(root, text="Calculate MST", command=calculate_mst)
button_calculate.pack()

output_label = tk.Label(root)
output_label.pack()

root.mainloop()
