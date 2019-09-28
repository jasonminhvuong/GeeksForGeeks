"""
    Trie is an efficient information retrieval data structure. Use this data
    structure to store Strings and search strings. Your task is to use TRIE 
    data structure and search the given string A. If found print 1 else 0.

    Input:
    The first line of input contains a single integer T denoting the number
    of test cases. Then T test cases follow. Each test case consists of three
    lines. First line of each test case consist of a integer N, denoting the
    number of element in a Trie to be stored. Second line of each test case
    consists of N space separated strings denoting the elements to be stored
    in the trie. Third line of each test case consists of a String A to be
    searched in the stored elements.
"""

class TreeNode:
    def __init__(self):
        self.is_end = False
        self.children = {}
    
class Trie:
    def __init__(self):
        self.root = TreeNode()
    
    def insert(self, word):
        node = self.root
        
        for ch in word:
            if ch not in node.children:
                node.children[ch] = TreeNode()
            
            node = node.children[ch]
        
        node.is_end = True
    
    def search(self, word):
        node = self.root
        
        for ch in word:
            if ch not in node.children:
                return False
                
            node = node.children[ch]
        
        return node.is_end

def main():
    for _ in range(int(input())):
        input()
        words = input().split()
        search_word = str(input())
        
        trie = Trie()
        for word in words:
            trie.insert(word)
        
        if trie.search(search_word):
            print(1)
        else :
            print(0)
        
if __name__ == '__main__':
    main()