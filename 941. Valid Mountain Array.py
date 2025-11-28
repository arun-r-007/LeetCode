class Solution(object):
    def validMountainArray(self, arr):
        n = len(arr)
        if n < 3:
            return False

        max_val = max(arr)
        max_idx = arr.index(max_val)

        if max_idx == 0 or max_idx == n - 1:
            return False

        for i in range(max_idx):
            if arr[i] >= arr[i + 1]:
                return False

        for j in range(max_idx, n - 1):
            if arr[j] <= arr[j + 1]:
                return False

        return True


a = Solution()
print(a.validMountainArray([0, 3, 2, 1]))  # Output: True
