"""
    Trie is an efficient information retrieval data structure. This data
    structure is used to store Strings and search strings, String stored
    can also be deleted so, Your task is to complete the function deleteKey
    to delete the given string A.The String A if exists in the larger String
    must be deleted from Trie. And if the string is deleted successfully
    than 1 will be printed.

    Input:
    The first line of input contains a single integer T denoting the number of
    test cases. Then T test cases follow. Each test case consists of three
    lines. First line of each test case consist of a integer N, denoting the
    number of element in a Trie to be stored. Second line of each test case
    consists of N space separated strings denoting the elements to be stored in
    the trie. Third line of each test case consists of a String A to be searched
    in the stored elements.
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

    def delete_helper(self, node, word, depth):
        if word == "":
            return True

        if depth == len(word):
            node.is_end = False
            return not node.children
        
        next_char = word[depth+1]

        if next_char not in node.children:
            return False
        
        can_del = self.delete_helper(node.children[next_char], word, depth+1)

        if can_del and len(node.children) == 1:
            del node.children[next_char]
            return True
        
        return False

    def delete(self, word):
        if self.search(word):
            self.delete_helper(self.root, word, -1)
            return True
        
        return False

def main():
    pass
        
if __name__ == '__main__':
    main()
