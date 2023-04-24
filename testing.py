"""
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.
"""

nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

current = nums[0]
maximum = nums[0]

for num in nums[1:]:
    if num > current + num:
        current = num
    else:
        current += num
    
    if current > maximum:
        maximum = current

print(maximum)


