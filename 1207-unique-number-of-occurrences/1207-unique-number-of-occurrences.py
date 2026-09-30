class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        hashmap = {}
        set1 = set()
        for num in arr:
            if num not in hashmap:
                hashmap[num] = 1
            else:
                hashmap[num] += 1
        
        for key, value in hashmap.items():
            if value in set1:
                return False
            set1.add(value)

        return True