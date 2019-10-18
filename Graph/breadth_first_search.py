def bfs(g,N):
    '''
    can use queue module already imported
    :param g: given adjacency list of graph
    :param N: number of nodes in N.
    :return: print the bfs of the graph from node 0, newline is given by driver code
    '''
    
    visited = set()
    q = []
    
    q.append(0)
    visited.add(0)
    
    while q:
        e = q.pop(0)
        print(e, end = ' ')
        for child in g[e]:
            if child not in visited:
                q.append(child)
                visited.add(child)