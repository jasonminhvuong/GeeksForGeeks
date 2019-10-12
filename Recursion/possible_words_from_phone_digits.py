"""
    Given a keypad as shown in diagram, and a n digit number, list all words
    which are possible by pressing these numbers. For example if input number
    is 234, possible words which can be formed are (Alphabetical order): adg 
    adh adi aeg aeh aei afg afh afi bdg bdh bdi beg beh bei bfg bfh bfi cdg
    cdh cdi ceg ceh cei cfg cfh cfi 
"""

class Solution:
    def print_words_phone_digits(self, number, keypad):
        if not number:
            return []

        digit = int(number[-1])
        number = number[:-1]
 
        prev_words = self.print_words_phone_digits(number, keypad)
        words = []
        
        if digit in keypad:
            if not prev_words:
                return keypad[digit]
            else:
                for c in keypad[digit]:
                    for word in prev_words:
                        words.append(word+c)
        
        return words

def main():
    keypad = {2:['a', 'b', 'c'], 3:['d', 'e', 'f'], 4:['g', 'h', 'i'], \
        5:['j', 'k', 'l'], 6:['m', 'n', 'o'], 7:['p', 'q', 'r', 's'], \
        8:['t', 'u', 'v'], 9:['w', 'x', 'y', 'z']}

    number = "234"
    sol = Solution()
    result = sol.print_words_phone_digits(number, keypad)
    result.sort()
    print(result)

if __name__ == "__main__":
    main()