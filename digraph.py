# -*- coding: utf-8 -*-

# Graph Models

class Node(object):

    def __init__(self, name):
        """Assumes name is a string"""
        self.name = name

    def getName(self):
        return self.name

    def __str__(self):
        return self.name


class Edge(object):

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


class Digraph():
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

    def childrenOf(self, node):
        return self.edges[node]

    def hasNode(self, node):
        return node in self.edges

    def getNode(self, name):
        for n in self.edges:
            if n.getName() == name:
                return n
        raise NameError(name)

    def __str__(self):
        result = ''
        for source in self.edges:
            for destination in self.edges[source]:
                result = result + source.getName() + '->' + destination.getName() + '\n'

        return result[:-1] # omit final newline


class Graph(Digraph):
    def addEdge(self, edge):
        Digraph.addEdge(self, edge)
        rev = Edge(edge.getDestination(), edge.getSource())
        Digraph.addEdge(self, rev)

# nodes are represented as the keys in a dictionary
# and the edges are represented by destinations as values
# in list associated with a source key


def buildCityGraph(graphType):
    g = graphType()

    cities = ('Boston', 'Providence', 'New York', 'Chicago',
              'Denver', 'Phoenix', 'Los Angeles') #Create 7 nodes
    
    for city in cities:
        g.addNode(Node(city))

    edges = [('Boston', 'Providence'),
             ('Boston', 'New York'),
             ('Providence', 'Boston'),
             ('Providence', 'New York'),
             ('New York', 'Chicago'),
             ('Chicago', 'Denver'),
             ('Chicago', 'Phoenix'),
             ('Denver', 'Phoenix'),
             ('Denver', 'New York'),
             ('Los Angeles', 'Boston')
             ]

    for edge in edges:
        g.addEdge(Edge(g.getNode(source)), Edge(g.getNode(destination)))

    return g

def printPath(path):
    """Assumes path is a list of nodes"""
    result = ''
    for i in range(len(path)):
        result = result + str(path[i])
        if i != len(path) - 1:
            result = result + '->'
    return result

#########################################################
g = buildCityGraph(Digraph)

printPath(g)















