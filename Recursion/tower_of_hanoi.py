"""
    The tower of Hanoi is a famous puzzle where we have three rods and N disks.
    The objective of the puzzle is to move the entire stack to another rod.
    You are given the number of discs N. Initially, these discs are in the
    rod 1. You need to print all the steps of discs movement so that all the
    discs reach the 3rd rod. Also, you need to find the total moves.
    Note: The discs are arranged such that the top disc is numbered 1 and the
    bottom-most disc is numbered N. Also, all the discs have different sizes
    and a bigger disc cannot be put on the top of a smaller disc. Refer the
    provided link to get a better clarity about the puzzle.

    Input:
    The first line of input is T denoting the number of testcases. T testcases
    follow. Each testcase contains a single line of input containing N.

    Output:
    For each testcase, print the steps and the total steps taken. Please see
    the example output to see the steps format.
"""

class Solution:
    def __init__(self):
        self.result = 0
    
    def print_helper(self, disk, src, dst):
        print("move disk " + str(disk) + " from rod " \
        + str(src) + " to rod " + str(dst))
    
    def tower_of_hanoi(self, disk, src, dst, aux):
        if disk == 1:
            self.result += 1
            self.print_helper(disk, src, dst)
            return
        
        self.tower_of_hanoi(disk-1, src, aux, dst)
        self.result += 1
        self.print_helper(disk, src, dst)
        self.tower_of_hanoi(disk-1, aux, dst, src)

def main():
    n = int(input())
    sol = Solution()
    
    for _ in range(n):
        sol.result = 0
        disk = int(input())
        sol.tower_of_hanoi(disk, 1, 3, 2)
        print(sol.result)

if __name__ == '__main__':
    main()