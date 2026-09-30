class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        hashmap1 = {}
        hashmap2 = {}

        if len(word1) != len(word2):
            return False
        
        for letter in word1:
            if letter not in hashmap1:
                hashmap1[letter] = 1
            else:
                hashmap1[letter] += 1
        
        for letter in word2:
            if letter not in hashmap2:
                hashmap2[letter] = 1
            else:
                hashmap2[letter] += 1

        return (hashmap1.keys() == hashmap2.keys() and sorted(hashmap1.values()) == sorted(hashmap2.values()))