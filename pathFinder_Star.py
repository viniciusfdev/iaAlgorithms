class Graph:
    def __init__(self, origin, destiny):
        self.nodes = {}
        self.origin = origin
        self.destiny = destiny
        self.border = {}
        self.found = False
        self.visited = []
 
    def start(self):
        print('Starting...')
        self.nodes = {
            'Oradea': {'h': 380, 'conn': {'Zerind': 71, 'Sibiu': 151}},
            'Zerind': {'h': 374, 'conn': {'Oradea': 71, 'Arad': 75}},
            'Arad': {'h': 366, 'conn': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118}},
            'Sibiu': {'h': 253, 'conn': {'Oradea': 151, 'Arad': 140, 'Fagaras': 99, 'Rimnicu Vikea': 80}},
            'Timisoara': {'h': 329, 'conn': {'Arad': 118, 'Lugoj': 111}},
            'Lugoj': {'h': 244, 'conn': {'Timisoara': 111, 'Mehadia': 70}},
            'Mehadia': {'h': 241, 'conn': {'Lugoj': 70, 'Dobreta': 75}},
            'Dobreta': {'h': 242, 'conn': {'Mehadia': 75, 'Craiova': 120}},
            'Fagaras': {'h': 176, 'conn': {'Sibiu': 99, 'Bucharest': 211}},
            'Rimnicu Vikea': {'h': 193, 'conn': {'Sibiu': 80, 'Pitesti': 97, 'Craiova': 148}},
            'Craiova': {'h': 160, 'conn': {'Dobreta': 120, 'Rimnicu Vikea': 148, 'Pitesti': 138}},
            'Pitesti': {'h': 101, 'conn': {'Rimnicu Vikea': 97, 'Craiova': 138, 'Bucharest': 101}},
            'Giurgiu': {'h': 77, 'conn': {'Bucharest': 90}},
            'Neamt': {'h': 234, 'conn': {'Iasi': 87}},
            'Vaslui': {'h': 199, 'conn': {'Iasi': 92, 'Urziceni': 142}},
            'Urziceni': {'h': 80, 'conn': {'Vaslui': 142, 'Bucharest': 85, 'Hirsova': 98}},
            'Eforie': {'h': 161, 'conn': {'Hirsova': 86}},
            'Iasi': {'h': 226, 'conn': {'Neamt': 87, 'Vaslui': 92}},
            'Hirsova': {'h': 151, 'conn': {'Eforie': 86, 'Urziceni': 98}},
            'Bucharest': {'h': 0, 'conn': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 86}}
        }

    def whoIsMinor(self):
        minor = list(self.border)[0]

        for node in self.border:
            if self.border[node]['dist']+self.nodes[node]['h'] < self.border[minor]['dist']+self.nodes[minor]['h']:
                minor = node

        return minor
    
    def incrementBorder(self, node_key):

        parents = self.border[node_key]['parents']
        parentDist = self.border[node_key]['dist']
        parent = {}
        parent[node_key] = parentDist    
        parents.append(parent)
        
        del self.border[node_key]
        self.visited.append(node_key)
        
        for node in self.nodes[node_key]['conn']:
            if(node not in self.visited):
                self.border[node] = { 'dist': self.nodes[node_key]['conn'][node]+parentDist,  'parents': parents }

        if self.border == {}:
            return True
        else:
            return False


    def getDeph(self):  
        if self.whoIsMinor() == self.destiny:
            self.found = True
            return True

        elif self.incrementBorder(self.whoIsMinor()):
            return False

        return self.getDeph()

    def getResult(self):
        if self.border[self.destiny]['parents'] == []:
            print('You dont search or dont have any result')
        else:    
            for node in self.border[self.destiny]['parents']:
                print(node)
            destiny = {}
            destiny[self.destiny] = self.border[self.destiny]['dist']
            print(destiny)

    def search(self):
        self.border[self.origin] = { 'dist': 0,  'parents': []}
        
        if self.getDeph() | self.found:
            self.getResult()
            print('\n^ Caminho ^')
        else:
            print('caminho nao encontrado')

if __name__ == "__main__":
    print("Insira a origem (ex: Craiova)")
    origin = input()
    graph = Graph(origin, "Bucharest")
    graph.start()
    print("Indo a bucharest...\n")
    graph.search()