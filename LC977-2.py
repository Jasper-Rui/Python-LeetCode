class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:

        # instead of brute force with time complexity O(nlogn)
        # using double pointers point from start and end
        # the max of squares are either at left or at right
        # compare two of them each time until left = right
        if len(nums) is 0:
            return nums

        if len(nums) is 1:
            nums[0] = nums[0] ** 2
            return nums

        start = 0
        end = len(nums) - 1

        while (nums[start] < 0):

            # figure out which one is larger, if start ** 2 >= end ** 2
            # then remove nums[start] by using nums.pop(start) because pop will remove the element and return it's value
            # and add it to the index end by using nums.insert(end, abs(value))
            # since we remove one element from left, index 'start' will automatically points to next value
            # so we do not need to update start value for now
            # 
            # else if start ** 2 < end ** 2, which means right side is larger than left, go to check next element from right
            # loop ends then start are equals to end

            if (nums[start] ** 2 >= nums[end] ** 2):
                tmp = nums.pop(start)
                nums.insert(end, abs(tmp))
                end -= 1
            else:
                end -= 1

        for i in range(0, len(nums)):
            nums[i] = nums[i] ** 2
        return nums


