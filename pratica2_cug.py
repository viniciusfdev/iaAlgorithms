class Graph:
    def __init__(self, origin, destiny):
        self.nodePath = []
        self.nodes = {}
        self.origin = origin
        self.destiny = destiny
        self.border = {}
        self.found = False
 
    def start(self):
        print('Starting...')
        self.nodes = {
            'Oradea': {'h': 380, 'conn': {'Zerind': 71, 'Sibiu': 151}},
            'Zerind': {'h': 374, 'conn': {'Oradea': 71, 'Arad': 75}},
            'Arad': {'h': 366, 'conn': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118}},
            'Sibiu': {'h': 253, 'conn': {'Oradea': 151, 'Arad': 140, 'Fagaras': 99, 'Rimnicu Vikea': 80}},
            'Timisoara': {'h': 329, 'conn': {'Arad': 118, 'Lugoj': 111}},
            'Lugoj': {'h': 244, 'conn': {'Timisoara': 111, 'Mehadia': 70}},
            'Mehadia': {'h': 241, 'conn': {'Logoj': 70, 'Dobreta': 75}},
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
            'Bucharest': {'h': 0, 'conn': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90, 'Urziceni': 86}}
        }

    def whoIsMinor(self):
        minor = list(self.border)[0]
        for node in self.border:
            if node['dist'] < minor:
                minor = node
        return minor

    def getDistance(self, node_key, parenthDist):
        return self.nodes[node_key]['h']+parenthDist
    
    def incrementBorder(self, node_key):
        parenthDist = self.border[node_key]['dist']
        del self.border[node_key]
        
        for node in self.nodes[node_key]['conn']:
            if self.border[node]:
                return
            else:
                self.border[node] = {
                    node: self.nodes[node_key]['h']+parenthDist
                }

        print(self.border)
        
        if self.border == {}:
            return False
        else:
            return True


    def getDeph(self):
        if self.whoIsMinor() == self.destiny:
            self.found = True
            return

        if self.incrementBorder(self.whoIsMinor()):
            return False

        return self.getDeph()


    def search(self):
        print('Searching...')
        self.incrementBorder(self.origin)
        if self.getDeph() | self.found:
            print('encontrei o caminho')
        else:
            print('caminho nao encontrado')

if __name__ == "__main__":
    graph = Graph('Arad', 'Bucharest')
    graph.start()
    graph.search()