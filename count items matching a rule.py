from typing import List
class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        keys= {"type": 0, "color": 1, "name" : 2 }
        index = keys[ruleKey]
        count = 0

        for i in items:
            if i[index] == ruleValue:
                count +=1
        return count

s= Solution()
print(s.countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "silver"))
print(s.countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "type", "phone"))
print(s.countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "name", "pixel"))
print(s.countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], "color", "blue"))
print(s.countMatches([["phone","blue","pixel"],["computer","silver","lenovo "],["phone","gold","iphone"]], "type", "computer")) 
