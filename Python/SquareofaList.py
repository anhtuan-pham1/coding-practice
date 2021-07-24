# https://binarysearch.com/problems/Square-of-a-List
# Using a regular way would take O(nlogn) because of the built in sorting function

def solve(nums):
    ans = []
    for i in nums:
        square = i ** 2
        ans.append(square)
    ans.sort()
    return ans

solve([-9, -2, 0, 2, 3])

# A better approach would be using 2 pointers which can be found https://binarysearch.com/problems/Square-of-a-List/editorials/250382
# This approach take O(n) (because O(n) for sorting square values and O(n) for reverse the list)

# def solve(self, nums):
#     ans = []
#     i, j = 0, len(nums) - 1
#     while i <= j:
#         if nums[i] ** 2 > nums[j] ** 2:
#             ans.append(nums[i] ** 2)
#             i += 1
#         else:
#             ans.append(nums[j] ** 2)
#             j -= 1
#     return list(reversed(ans))
