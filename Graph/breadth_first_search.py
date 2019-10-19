"""
    Given N and E, the number of nodes and edges in a directed graph. The task
    is to do Breadth First Search of this graph.

    Input:
    The first line of input contains the number of test cases T. For each test
    case, the first line of input contains N and E separated by space, and next
    line contains 2*E numbers (E pairs as X Y) are given in the next line which
    represents an edge from X to Y.

    Output:
    For each testcase, print the BFS of the graph starting from 0.

    Note: The expected output button always produces BFS starting from node 0.

    User Task:
    Since, this is a functional problem, your task is to complete the function
    bfs() which do BFS of the given graph starting from node 0 and prints the
    nodes in BFS order.
"""
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