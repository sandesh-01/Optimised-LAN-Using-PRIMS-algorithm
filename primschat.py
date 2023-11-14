import tkinter as tk
from tkinter import ttk

class NetworkOptimizerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Network Optimizer")

        self.label = ttk.Label(root, text="Enter the number of buildings:")
        self.label.pack(pady=10)

        self.building_entry = ttk.Entry(root)
        self.building_entry.pack(pady=10)

        self.button = ttk.Button(root, text="Next", command=self.get_distances)
        self.button.pack(pady=10)

    def get_distances(self):
        num_buildings = int(self.building_entry.get())
        self.label.config(text="Enter distances between buildings:")

        distance_entries = []
        for i in range(num_buildings):
            for j in range(i + 1, num_buildings):
                label_text = f"Distance between Building {i + 1} and Building {j + 1}:"
                label = ttk.Label(self.root, text=label_text)
                label.pack(pady=5)

                entry = ttk.Entry(self.root)
                entry.pack(pady=5)

                distance_entries.append(entry)

        submit_button = ttk.Button(self.root, text="Submit", command=lambda: self.optimize_network(distance_entries))
        submit_button.pack(pady=10)

    def optimize_network(self, distance_entries):
        distances = [float(entry.get()) for entry in distance_entries]
        num_buildings = int(self.building_entry.get())

        adjacency_matrix = [[float('inf')] * num_buildings for _ in range(num_buildings)]

        index = 0
        for i in range(num_buildings):
            for j in range(i + 1, num_buildings):
                adjacency_matrix[i][j] = distances[index]
                adjacency_matrix[j][i] = distances[index]
                index += 1

        optimized_network = self.prim_algorithm(adjacency_matrix)
        print("Optimized Network:", optimized_network)

    def prim_algorithm(self, graph):
        num_vertices = len(graph)
        min_span_tree = []

        # Choose the starting vertex (0 in this case)
        start_vertex = 0

        # List to keep track of visited vertices
        visited = [False] * num_vertices

        # Mark the start vertex as visited
        visited[start_vertex] = True

        while len(min_span_tree) < num_vertices - 1:
            min_weight = float('inf')
            min_edge = None

            # Iterate over all vertices
            for i in range(num_vertices):
                if visited[i]:
                    for j in range(num_vertices):
                        if not visited[j] and graph[i][j] < min_weight:
                            min_weight = graph[i][j]
                            min_edge = (i, j)

            if min_edge:
                min_span_tree.append(min_edge)
                visited[min_edge[1]] = True

        return min_span_tree


if __name__ == "__main__":
    root = tk.Tk()
    app = NetworkOptimizerApp(root)
    root.mainloop()
