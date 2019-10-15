"""
    Given number of edges 'E' and vertices 'V' of a bidirectional graph. Your
    task is to build a graph through adjacency list and print the adjacency
    list for each vertex.

    Input:
    The first line of input is T denoting the number of testcases.Then first
    line of each of the T contains two positive integer V and E where 'V' is
    the number of vertex and 'E' is number of edges in graph. Next, 'E' line
    contains two positive numbers showing that there is an edge between these two vertex.

    Output:
    For each vertex, print their connected nodes in order you are pushing them inside the
    list . See the  given  example.
"""

class Graph:
    def __init__(self, v):
        self.adj_list = {}
        for i in range(v):
            self.adj_list[i] = []
        
    def add_edge(self, src, dst):
        self.adj_list[src].append(dst)
    
    def print_graph(self):
        for k, v in self.adj_list.items():
            print(str(k), end="")
            
            for n in v:
                print("-> " + str(n), end="")
                
            print()

def main():
    t = int(input())
    
    for _ in range(t):
        d = input().split()
        v, e = int(d[0]), int(d[1])
        graph = Graph(v)
        for _ in range(e):
            s = input().split()
            v1, v2 = int(s[0]), int(s[1])
            graph.add_edge(v1, v2)
            graph.add_edge(v2, v1)
        
        graph.print_graph()

if __name__ == '__main__':
    main()
    