class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        sum = 0
        i = 0
        result = 10000001

        for j in range(0, len(nums)):
            sum += nums[j]
            while (sum >= target):
                tmp_length = j - i + 1
                result = tmp_length if tmp_length < result else result
                sum -= nums[i]
                i += 1

        return result if result is not 10000001 else 0
