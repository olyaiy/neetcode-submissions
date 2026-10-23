class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        letters_s = {}
        letters_t = {}

        for letter in s:

            if letter in letters_s: 
                letters_s[letter] += 1
            else: 
                letters_s[letter] = 1


        for letter in t:
            if letter in letters_t: 
                letters_t[letter] += 1
            else: 
                letters_t[letter] = 1

        print('letters_s is ', letters_s)
        print('letters_t is ', letters_t)

        return letters_s == letters_t
        


        