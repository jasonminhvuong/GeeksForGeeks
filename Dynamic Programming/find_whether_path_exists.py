"""
    Given a N X N matrix (M) filled with 1, 0, 2, 3. The task is to find
    whether there is a path possible from source to destination, while
    traversing through blank cells only. You can traverse up, down, right and
    left.

    A value of cell 1 means Source.
    A value of cell 2 means Destination.
    A value of cell 3 means Blank cell.
    A value of cell 0 means Blank Wall.
    Note: there is only single source and single destination.

    Input:
    The first line of input is an integer T denoting the no of testcases. Then
    T test cases follow. Each test case consists of 2 lines. The first line of
    each test case contains an integer N denoting the size of the square
    matrix. Then in the next line are N*N space separated values of the
    matrix (M).

    Output:
    For each test case in a new line print 1 if the path exist from source to
    destination else print 0.
"""

from collections import defaultdict

class Solution:
    def get_pos(self, i, j, n):
        return (i * n) + j
        
    
    def matrix_to_adj_list(self, m, n):
        adj_list = defaultdict(set)
        for i in range(n):
            for j in range(n):
                u = self.get_pos(i, j, n)
                
                if m[i][j] == 0:
                    continue
                
                if i != 0 and m[i-1][j] != 0:
                    v = self.get_pos(i-1, j, n)
                    adj_list[u].add(v)
                    adj_list[v].add(u)
                
                if i != n-1 and m[i+1][j] != 0:
                    v = self.get_pos(i+1, j, n)
                    adj_list[u].add(v)
                    adj_list[v].add(u)
                    
                if j != 0 and m[i][j-1] != 0:
                    v = self.get_pos(i, j-1, n)
                    adj_list[u].add(v)
                    adj_list[v].add(u)
                 
                if j != n-1 and m[i][j+1] != 0:
                    v = self.get_pos(i, j+1, n)
                    adj_list[u].add(v)
                    adj_list[v].add(u)                   
                    
        return adj_list
        
    def find_if_path_exists(self, src, dst, m, n):
        adj_list = self.matrix_to_adj_list(m, n)
        queue = []
        visited = set()
        queue.append(src)
        visited.add(src)
        
        while queue:
            node = queue.pop(0)
            
            if node == dst:
                return 1
            
            for e in adj_list[node]:
                if e not in visited:
                    visited.add(e)
                    queue.append(e)
        
        return 0
    
def main():
    t = int(input())
    sol = Solution()
    
    for _ in range(t):
        n = int(input())
        vals = input().split()
        m = []
        src = 0
        dst = 0
    
        for i in range(n):
            row = []
            for j in range(n):
                val = int(vals.pop(0))
                
                if val == 1:
                    src = (i*n)+j
                elif val == 2:
                    dst = (i*n)+j
                
                row.append(val)
                
            m.append(row)
            
        print(sol.find_if_path_exists(src, dst, m, n))
        

if __name__ == '__main__':
    main()