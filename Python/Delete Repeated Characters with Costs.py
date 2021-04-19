# https://binarysearch.com/problems/Delete-Repeated-Characters-with-Costs

def solve( s, nums):
    cost = 0
    for i in range (0,len(s)-1):
        if s[i] == s[i+1]:
            if nums[i] < nums[i+1]:
                cost += nums[i]
            else:
                cost += nums[i+1]
                nums[i+1] = nums[i]
    return cost
