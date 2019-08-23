graph = {'a':{'b', 'e'},
             'b':{'a', 'e', 'f', 'g', 'c'},
             'c':{'b', 'g', 'h', 'd'},
             'd':{'c', 'h'},
             'e':{'a', 'b', 'f', 'h'},
             'f':{'e', 'b', 'g', 'h'},
             'g':{'f', 'b', 'c', 'h'},
             'h':{'e', 'f', 'g', 'c', 'd'}}


# Sorting the graph according to its degree (higher degrees come first)
ordered_vertices = sorted(graph, key=lambda x: len(graph[x]), reverse=True)
# List with vertices that have different colors
colored_vertices = []
# While the ordered_vertices is not empty:
while ordered_vertices:
    # The vertice with higher degree "chooses" its color and is removed from the original list (ordered_vertices must be empty to stop the loop)
    colored_vertices.append(ordered_vertices[0])
    del(ordered_vertices[0])
    # temp variable keeps adjacent vertices that should not be colored
    temp = graph[colored_vertices[-1]]
    for j in ordered_vertices:
        # If a vertice has not yet been colored and is not adjacent to the last colored vertice, they could have the same color.
        if j not in colored_vertices and j not in temp:
            ordered_vertices.remove(j)
print('{} colors needed to paint the map'.format(len(colored_vertices)))


