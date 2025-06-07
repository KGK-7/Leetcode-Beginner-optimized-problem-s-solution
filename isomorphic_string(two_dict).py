class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        map_st={}
        map_ts={}

        for ch_s,ch_t in zip(s,t):
            if map_st.get(ch_s) is not None:
                if map_st[ch_s] != ch_t:
                    return False
            elif map_ts.get(ch_t) is not None:
                if map_ts[ch_t] != ch_s:
                    return False
            
            map_st[ch_s]=ch_t
            map_ts[ch_t]=ch_s
            
        return True

# Example usage:
sol = Solution()
print(sol.isIsomorphic("egg", "add"))  # Output: True
print(sol.isIsomorphic("foo", "bar"))  # Output: False
print(sol.isIsomorphic("paper", "title"))  # Output: True
print(sol.isIsomorphic("ab", "aa"))  # Output: False
