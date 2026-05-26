class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #n = len(nums)
        #prefix = [1] * n
        #suffix = [1] * n
        #for i in range(1, n):
        #    prefix[i] = prefix[i - 1] * nums[i - 1]
        #for i in range(n - 2, -1, -1):
        #    suffix[i] = suffix[i + 1] * nums[i + 1]
        #return [prefix[i] * suffix[i] for i in range(n)]
        # First pass: result[i] = product of everything to the left of i
        n = len(nums)
        result = [1] * n
        for i in range(1, n):
            result[i] = result[i - 1] * nums[i - 1]

        # Second pass: multiply by product of everything to the right
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result