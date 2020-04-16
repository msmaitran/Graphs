from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    graph = Graph()

    for pair in ancestors:
        for relationship in pair:
            if relationship not in graph.vertices:
                graph.add_vertex(relationship)
        parent = pair[0]
        child = pair[1]
        graph.add_edge(parent, child)

    paths = []
    for relationship in graph.vertices:
        if graph.bfs(relationship, starting_node) is not None:
            if len(graph.bfs(relationship, starting_node)) > 1:
                paths.append(graph.bfs(relationship, starting_node))

    if len(paths) == 0:
        return -1
    
    return max(paths, key=len)[0]