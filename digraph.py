# Graph Models

class node(object):

    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


class edge(object):

    def __init__(self, source, destination):
        """Assumes source and destination are nodes"""
        self.source = source
        self.destination = destination

    def getSource(self):
        return self.source

    def getDestination(self):
        return self.Destination

    def __str__(self):
        return self.source.getName() + '->' + self.destination.getName()


class digraph():
    """edges is a dict mapping each node to a list of
    its children"""

    def __init__(self):
        self.edges = {}

    def addNode(self, node):
        if node in self.edges:
            raise ValueError('Duplicate Node')
        else:
            self.edges[node] = []

    def addEdge(self, edge):
        source = edge.getSource()
        destination = edge.getDestination()

        if not (source in self.edges and destination in self.edges):
            raise ValueError('Node not in graph')
        self.edges[source].append(destination)




        
