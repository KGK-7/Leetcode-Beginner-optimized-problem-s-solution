class Solution(object):
    def isIsomorphic(self, s, t):
        mapp={}
        used_t=set()

        for ch_s,ch_t in zip(s,t):
            if ch_s in mapp:
                if mapp[ch_s] != ch_t:
                    return False
            else:
                if ch_t in used_t:
                    return False
                
                mapp[ch_s]=ch_t
                used_t.add(ch_t)
        return True

        # Example usage
if __name__ == "__main__":
    sol = Solution()
    print(sol.isIsomorphic("egg", "add"))  # True
    print(sol.isIsomorphic("foo", "bar"))  # False
    print(sol.isIsomorphic("paper", "title"))  # True