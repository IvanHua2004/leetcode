class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        pref = strs[0]
        prefLen = len(pref)

        for s in strs[1:]:
            while pref != s[0:prefLen]:
                prefLen -= 1
                if prefLen == 0:
                    return ""

                pref = pref[0:prefLen]
        return pref        
        