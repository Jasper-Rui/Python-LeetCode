class Solution:
    def search(self, nums: List[int], target: int) -> int:
        if target < nums[0]:
            return -1

        if len(nums) == 1 and target == nums[0]:
            return 0

        for i in range(len(nums)):
            if nums[i] == target:
                return i

        return -1    