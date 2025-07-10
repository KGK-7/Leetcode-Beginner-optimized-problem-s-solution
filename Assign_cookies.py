class Solution:
    def quick_sort(self, arr, left, right):
        if left >= right:
            return

        pivot = arr[right]         # Choose rightmost element as pivot
        i = left                   # Index to place smaller elements

        for j in range(left, right):
            if arr[j] <= pivot:
                arr[i], arr[j] = arr[j], arr[i]
                i += 1

        arr[i], arr[right] = arr[right], arr[i]  # Place pivot in correct position

        self.quick_sort(arr, left, i - 1)         # Sort left part
        self.quick_sort(arr, i + 1, right)        # Sort right part

    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        self.quick_sort(g, 0, len(g) - 1)
        self.quick_sort(s, 0, len(s) - 1)

        child = 0
        cookie = 0
        content_children = 0

        while child < len(g) and cookie < len(s):
            if s[cookie] >= g[child]:
                content_children += 1
                child += 1
            cookie += 1

        return content_children
