# https://binarysearch.com/problems/Sum-of-Two-Numbers-Less-Than-Target
# Used 2 pointers on a sorted array
# O(nlogn) since default sorting algorithm in Python is Tim sort

def solve( nums, target):
    nums.sort()
    pointer1 = 0
    pointer2 = (len(nums) - 1)
    min_val = -100
    while pointer1 < pointer2:
        #print(min_val)
        total = nums[pointer1] + nums[pointer2]
        #print(total)
        if total < target:
            if total > min_val:
                min_val = total
            pointer1 += 1
        else:
            pointer2 -= 1
    print(min_val)
    return min_val

solve([-2, -3, -1], -4)