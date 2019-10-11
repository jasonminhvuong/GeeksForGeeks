"""
    Given a 2D screen, location of a pixel in the screen ie(x,y) and a
    color(K), your task is to replace color of the given pixel and all
    adjacent(excluding diagonally adjacent) same colored pixels with the
    given color K.

    Example:

    {{1, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 1, 1, 1, 1, 0, 0},
    {1, 0, 0, 1, 1, 0, 1, 1},
    {1, 2, 2, 2, 2, 0, 1, 0},
    {1, 1, 1, 2, 2, 0, 1, 0},
    {1, 1, 1, 2, 2, 2, 2, 0},
    {1, 1, 1, 1, 1, 2, 1, 1},
    {1, 1, 1, 1, 1, 2, 2, 1},
    };

    x=4, y=4, color=3 

    {{1, 1, 1, 1, 1, 1, 1, 1},
    {1, 1, 1, 1, 1, 1, 0, 0},
    {1, 0, 0, 1, 1, 0, 1, 1}, 
    {1, 3, 3, 3, 3, 0, 1, 0},
    {1, 1, 1, 3, 3, 0, 1, 0},
    {1, 1, 1, 3, 3, 3, 3, 0},
    {1, 1, 1, 1, 1, 3, 1, 1},
    {1, 1, 1, 1, 1, 3, 3, 1}, };

    Note: Use zero based indexing.

    Input:
    The first line of input contains an integer T denoting the no of test
    cases. Then T test cases follow. The first line of each test case contains
    Two integers N and M denoting the size of the matrix. Then in the next
    line are N*M space separated values of the matrix. Then in the next line
    are three values x, y and K.

    Output:
    For each test case print the space separated values of the new matrix.
"""

class Solution:
    def flood_fill(self, matrix, row, col, dst_color, src_color):
        if not matrix or row < 0 or \
        row >= len(matrix) or col < 0 or col >= len(matrix[0]):
            return
        
        if src_color == -1:
            src_color = matrix[row][col]
            
        if matrix[row][col] != src_color:
            return
        
        matrix[row][col] = dst_color
        
        self.flood_fill(matrix, row+1, col, dst_color, src_color)
        self.flood_fill(matrix, row, col+1, dst_color, src_color)
        self.flood_fill(matrix, row-1, col, dst_color, src_color)
        self.flood_fill(matrix, row, col-1, dst_color, src_color)
    
def main():
    n = int(input())
    sol = Solution()
    
    for _ in range(n):
        size = input().split()
        rows = int(size[0])
        cols = int(size[1])
        pixels = input().split()
        vals = input().split()
        matrix = []

        for i in range(rows):
            row = []
            for j in range(cols):
                elem = pixels.pop(0)
                row.append(elem)
            
            matrix.append(row)
            
        x, y, k = int(vals[0]), int(vals[1]), int(vals[2])
        
        sol.flood_fill(matrix, x, y, k, -1)
        
        for i in range(rows):
            for j in range(cols):
                if i == rows-1 and j == cols-1:
                    print(matrix[i][j])
                else:
                    print(matrix[i][j], end=" ")

if __name__ == '__main__':
    main()