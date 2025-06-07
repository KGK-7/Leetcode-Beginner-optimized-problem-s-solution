class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_st = {}
        map_ts = {}

        for ch_s, ch_t in zip(s, t):
            if ch_s in map_st:
                if map_st[ch_s] != ch_t:
                    return False
            elif ch_t in map_ts:
                if map_ts[ch_t] != ch_s:
                    return False
            
            map_st[ch_s] = ch_t
            map_ts[ch_t] = ch_s

        return True
# Example usage:
sol = Solution()
print(sol.isIsomorphic("egg", "add"))  # Output: True
print(sol.isIsomorphic("foo", "bar"))  # Output: False
print(sol.isIsomorphic("paper", "title"))  # Output: True
print(sol.isIsomorphic("ab", "aa"))  # Output: False    
print(sol.isIsomorphic("abc", "def"))  # Output: True