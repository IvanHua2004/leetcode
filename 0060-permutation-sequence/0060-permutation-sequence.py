class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        arr = list(range(1, n+1))
        for _ in range(k-1):
            self.nextPermutation(arr)
        return "".join(map(str, arr))


    def nextPermutation(self, arr: List[int]):
        i = len(arr) - 2
        while i >= 0 and arr[i] >= arr[i+1]:
            i -= 1
        
        j = len(arr) - 1
        while arr[j] <= arr[i]:
            j -= 1
        
        arr[i], arr[j] = arr[j], arr[i]
        arr[i+1:] = reversed(arr[i+1:])