"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        """
        Add a vertex to the graph.
        """
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        """
        Add a directed edge to the graph from v1 to v2.
        """
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("YOU MESSING UP")

    def get_neighbors(self, vertex_id):
        """
        Get all neighbors (edges) of a vertex.
        """
        return self.vertices[vertex_id]

    def bft(self, starting_vertex):
        """
        Print each vertex in breadth-first order
        beginning from starting_vertex.
        """

        # use a queue to keep track of the traversing
        # variable of visited to keep track, so not to repeatedly traverse
        # start by adding starting vertex to queue
        # if the vertex does not exist in the visited set
        # get all the neighbors of the (starting) vertex
        # add each neighbor to the queue
        # print the starting vertex
        # add the vertex to the visited set
        # while the queue is not empty, repeat

        q = Queue()
        visited = set()
        q.enqueue(starting_vertex)

        while q.size() > 0:
            vertex = q.dequeue()
            if vertex not in visited:
                neighbors = self.get_neighbors(vertex)
                for neighbor in neighbors:
                    q.enqueue(neighbor)
                print(vertex)
                visited.add(vertex)

    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        
        # stack to keep track of vertices that need to be traversed
        s = Stack()
        # set - visited - to keep track of visited vertices
        visited = set()
        # add the starting vertex to the stack
        s.push(starting_vertex)

        # while the stack is not empty
        while s.size() > 0:
            # pop off a vertex from the stack
            vertex = s.pop()
            # if the vertex is not visited
            if vertex not in visited:
                # find its neighbors and add to the stack
                neighbors = self.get_neighbors(vertex)
                for neighbor in neighbors:
                    s.push(neighbor)
                # mark the vertex as visited
                visited.add(vertex)
                # print its value
                print(vertex)


    def dft_recursive(self, starting_vertex, visited=set()):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        
        # print starting vertex
        print(starting_vertex)
        # find neighbors of starting vertex
        neighbors = self.get_neighbors(starting_vertex)
        # for each neighbor 
        visited.add(starting_vertex)
        for neighbor in neighbors:
            # recursively call dft recursive on it if neighbor is not already visited
            if neighbor not in visited:
                self.dft_recursive(neighbor)

    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        
        # queue to keep track of path
        q = Queue()
        # visited to keep track of what's been visited
        visited = set()
        # add starting vertex to the queue, as a list
        q.enqueue([starting_vertex])

        # while the queue is not empty
        while q.size():
            # path equal to first one in the queue
            path = q.dequeue()
            # if the path's last element is equal to the destination, return path
            if path[-1] == destination_vertex:
                return path
            # otherwise, 
            # find the neighbors of the current vertex
            neighbors = self.get_neighbors(path[-1])
            # iterate through all the neighbors of current vertex 
            for neighbor in neighbors:
                # if neighbor is not in visited,
                if neighbor not in visited:
                    # then add that neighbor to current paths end
                    new_path = list(path)
                    new_path.append(neighbor)
                    # add this new path to the queue
                    q.enqueue(new_path)
                    # add the vertex to visited
            visited.add(path[-1])


    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        # stack to keep track of path
        s = Stack()
        # visited to keep track of which vertices have been visited
        visited = set()
        # add starting vertex to the stack, as a list
        s.push([starting_vertex])

        # while the stack is not empty
        while s.size():
            # path equal to the popped item from stack, aka last
            path = s.pop()
            # if the path's last element is equal to the destination, return path
            if path[-1] == destination_vertex:
                return path
            # otherwise
            # find the neighbors of the current vertex
            neighbors = self.get_neighbors(path[-1])
            # iterate through all the neighbors of current vertex
            for neighbor in neighbors:
                # if neighbor is not in visited
                if neighbor not in visited:
                    # then add that neighbor to current paths end
                    new_path = list(path)
                    new_path.append(neighbor)
                    # add this new path to the stack
                    s.push(new_path)
                    # add the vertex to visited
            visited.add(path[-1])

    def dfs_recursive(self, vertex, destination_vertex, visited=set(), path=[]):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        visited.add(vertex)
        path = path + [vertex]

        if vertex == destination_vertex:
            return path
        for neighbor in self.get_neighbors(vertex):
            if neighbor not in visited:
                result = self.dfs_recursive(neighbor, destination_vertex, visited, path)
                if result:
                    return result

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    print('BFT')
    graph.bft(1)

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    print('DFT')
    graph.dft(1)
    print('DFT recursive')
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print('BFS')
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print('DFS')
    print(graph.dfs(1, 6))
    print('DFS recursive')
    print(graph.dfs_recursive(1, 6))
