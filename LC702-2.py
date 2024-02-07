class Solution:
    def search(self, nums: List[int], target: int) -> int:

        start = 0
        end = len(nums) - 1

        while (start <= end):

            mid = (start + end) // 2

            if target == nums[mid]:
                return mid

            # locate in left
            elif nums[mid] > target:
                end = mid - 1

            # locate in right
            elif nums[mid] < target:
                start = mid + 1

        return -1