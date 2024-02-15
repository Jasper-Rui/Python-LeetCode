class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        min_length = 100001
        for i in range(0, len(nums)):
            sum = nums[i]
            if sum < target:
                for j in range(i + 1, len(nums)):
                    sum += nums[j]
                    if sum >= target:
                        min_length = j - i + 1 if j - i + 1 < min_length else min_length
            else:
                min_length = 1
                break

        return 0 if min_length == 100001 else min_length

