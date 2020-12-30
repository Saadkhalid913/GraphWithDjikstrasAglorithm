'''
Directed graph data structure by Saadkhalid913
'''


# Necessary imports from supplimentry module 
from supplementary import priorityqueue, stack, ToPath

# main directed graph class

class Graph():
    '''
    A graph object with adjacency list
    
    Methods:

    Add
    -------------------------------------------------------
    Takes multiple arguments of any datatype and initializes
    node in graph

    -------------------------------------------------------

    view
    -------------------------------------------------------
    Prints all nodes along with edges and weights as 
    key-value pairs 

    -------------------------------------------------------

    addedge
    -------------------------------------------------------
    Takes 3 positional arguments a, b, weight
    if a and b are not in graph AssertionError
    will be raised. Weight must be int > 0 or
    ValueError will be raised. 

    -------------------------------------------------------

    shortestpath
    -------------------------------------------------------
    Takes 2 positional arguments, Tonode and Fromnode
    takes 1 Kwarg "returntype" either "path" or "tuple"
    default="path" if returntype="tuple" method will return
    a tuple with 
    item at index -1 being distance between 2 nodes and
    items index 0 through -1 being nodes in sequential 
    order in path from node A to B
    if no path exists where distance < inf method will
    return inf
    '''
    def __init__(self):
        self.adjacencylist = {}
        self.nodes = []
    def __contains__(self, node):
        return node in self.nodes
    def __repr__(self):
        return str(self.adjacencylist)
    def __iter__(self):
        return iter(self.nodes)

    def add(self, *args):
        for node in args:
            if node in self:
                pass
            else:
                self.nodes.append(node)
                self.adjacencylist[node] = {}

    def view(self):
        for node in self:
            print(f"{node}: {self.adjacencylist[node]}") 
    
    def addedge(self, a,b,weight: int):
        assert a in self and b in self, "Both nodes must be in graph"
        self.adjacencylist[a][b] = weight

    def shortestpath(self, a,b, returntype="path"):
        '''
        Takes 2 positional arguments, Tonode and Fromnode
        takes 1 Kwarg "returntype" either "path" or "tuple"
        default="path" if returntype="tuple" method will return
        a tuple with 
        item at index -1 being distance between 2 nodes and
        items index 0 through -1 being nodes in sequential 
        order in path from node A to B
        if no path exists where distance < inf method will
        return inf
        '''
        assert a in self and b in self, "Both nodes must be in graph!"

        visited = set()
        distances = {node : float("inf") for node in self}
        distances[a] = 0

        PreviousNodes = {} 

        Q = priorityqueue()
        Q.add((a,0))
        
        while not Q.isempty():
            node = Q.remove()[0]
            visited.add(node)
            for ToNode in self.adjacencylist[node]:
                if ToNode in visited:
                    continue

                current_distance = distances[ToNode]
                if current_distance > distances[node] + self.adjacencylist[node][ToNode]:
                    distances[ToNode] = distances[node] + self.adjacencylist[node][ToNode]
                    PreviousNodes[ToNode] = node
                
                Q.add((ToNode, self.adjacencylist[node][ToNode]))

        if distances[b] == float("inf"):
            return float("inf")
        if returntype.lower() == "path":
            return " -> ".join(map(str, ToPath(a,b,PreviousNodes, stack()))) + " Distance: %s" % distances[b]
        elif returntype.lower() == "tuple":
            return tuple(ToPath(a,b,PreviousNodes, stack()) + [distances[b]])

