'''
    Your task is to implement the function strstr. The function takes two
    strings as arguments (s,x) and  locates the occurrence of the string x in
    the string s. The function returns and integer denoting the first
    occurrence of the string x in s.

	Your task is to return the index of the pattern
	present in the given string.
	
	Function Arguments: s (given text), p(given pattern)
	Return Type: Integer.
	
'''
def strstr(s,p):
    
    for i in range(len(s)):
        if s[i] != p[0]:
            continue
        
        found = True
        
        for j in range(len(p)):
            if i+j >= len(s) or s[i+j] != p[j]:
                found = False
                break
            
        if found:
            return i
            
    return -1