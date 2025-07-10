def findLucky(arr):
    freq = {}

    for i in range(len(arr)):
        if arr[i] in freq:
            freq[arr[i]] += 1
        else:
            freq[arr[i]] = 1

    lucky = -1
    for key in freq:
        if key == freq[key]:
            lucky = max(lucky, key)

    return lucky
