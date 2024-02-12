nums = [0,1,2,2,3,0,4,2]
val = 2
count = 0

for i in range(len(nums)):
    if i + count >= len(nums) - 1:
        break

    # loop from beginning, if find one val, replace it with the last non-val element
    # to do that, we need a value to track last non-val target

    if nums[i] is val:
        tar = len(nums) - count - 1

        while 1 > 0:
            if nums[tar] is not val:

                break
            tar -= 1
        # till now, nums[tar] is the one that non-val
        # replace it with nums[i]

        nums[i] = nums[tar]
        nums[tar] = val
        count += 1


print(len(nums) - count)
print(nums)