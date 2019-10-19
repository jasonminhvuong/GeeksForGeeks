"""
    Given N nodes and E edges of a graph. The task is to do depth first
    traversal of the graph.

    Note: Use recursive approach.

    Input:
    First line of input contains number of testcases T. For each testcase.
    First line of each testcase contains number of nodes and edges seperated by
    space and next line contains N pairs of integers (X and Y each) where X Y
    means an edge from X to Y.

    Output:
    For each testcase, print the nodes while doing DFS starting from node 0.

    Your task:
    The task is to complete the function dfs() which should do the depth first
    traversal of given graph and prints the node in DFS order.
"""

def dfs_helper(g, v, visited):
    print(v, end=" ")
    
    for e in g[v]:
        if e not in visited:
            visited.add(e)
            dfs_helper(g, e, visited)

def dfs(g,N):
    '''
    :param g: given adjacency list of graph
    :param N: number of nodes in N.
    :return: print the dfs of the graph from node 0, newline is given by driver code
    '''
    
    visited = set()
    visited.add(0)
    dfs_helper(g, 0, visited)