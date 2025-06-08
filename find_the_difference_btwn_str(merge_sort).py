def mergesort(arr):
    if len(arr)<=1:
        return arr
    
    mid=len(arr)//2
    left_half = mergesort(arr[:mid])
    right_half = mergesort(arr[mid:])

    sorted_arr =[]
    i=j=0

    while i<len(left_half) and j <len(right_half):
        if left_half[i] < right_half[j]:
            sorted_arr.append(left_half[i])
            i+=1
        else:
            sorted_arr.append(right_half[j])
            j+=1

    while i<len(left_half):
        sorted_arr.append(left_half[i])
        i+=1
    while j <len(right_half):
        sorted_arr.append(right_half[j])
        j+=1
    
    return sorted_arr
class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        sorted_s = mergesort(list(s))
        sorted_t = mergesort(list(t))

        for i in range(len(sorted_s)):
            if sorted_s[i] != sorted_t[i]:
                return sorted_t[i]

        return sorted_t[-1]        
# Example usage:
if __name__ == "__main__":
    s = "abcd"
    t = "abcde"
    solution = Solution()
    print(solution.findTheDifference(s, t))  # Output: 'e'
    