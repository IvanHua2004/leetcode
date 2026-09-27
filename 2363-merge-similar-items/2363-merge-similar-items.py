class Solution:
    def mergeSimilarItems(self, items1: list[list[int]], items2: list[list[int]]) -> list[list[int]]:
        hashmap = {}
        res = []

        for i in range(len(items1)):
            hashmap[items1[i][0]] = items1[i][1]

        for i in range(len(items2)):
            if items2[i][0] not in hashmap:
                hashmap[items2[i][0]] = items2[i][1]
            else:
                hashmap[items2[i][0]] += items2[i][1]

        for key, value in hashmap.items():
            res.append([key, value])

        return sorted(res)