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