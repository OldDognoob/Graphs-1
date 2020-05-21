import sys
sys.path.insert(0, '../graph/')

from graph import Graph

def earliest_ancestor(ancestors, starting_node):
    '''
    input: list of ancestors - in tuple form & starting node
      - first value in tuple represents parent
      - second value in tuple represents child
      - starting node is node for which earliest ancestor must be found

    output: earliest ancestor of the starting node

    plan:
    **setting up your graph
    create a graph
    iterate through each tuple in ancestors list
    if any one of the vertices does not exist in the graph, add it
    then connect the two vertices, via an edge
    NOW, you have a graph

    **you want to find the oldest ancestor, aka the one furthest away
    instantiate a longest path variable, set to 0
    use your DFS method on each node, with following parameters
      - starting vertex is each node you are iterating over
      - destination vertex is the same as earliest ancestor's starting_node parameter
    save this search to a path variable
    if this path is greater than previous paths, then update longest path to this path
    if longest path is equal to 0, return value of -1
      - indicates no such path is found
    return first vertex / node of longest path
    '''

    # setting up your graph
    g = Graph()

    for par_child in ancestors:
        parent = par_child[0]
        child = par_child[1]

        if parent not in g.vertices:
            g.add_vertex(parent)
        if child not in g.vertices:
            g.add_vertex(child)

        g.add_edge(parent, child)

    # finding the oldest ancestor
    longest_path = [1]

    for vertex in g.vertices:
        path = g.dfs(vertex, starting_node)

        if path and len(path) > len(longest_path):
            longest_path = path
    
    if longest_path == [1]:
        return -1
    
    return longest_path[0] # returns the first vertex/node aka 'earliest ancestor' for a path to starting_node
    
