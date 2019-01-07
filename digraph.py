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
    pass
