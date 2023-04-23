nums = [1,2,3,4]
queries = [[1,0],[-3,1],[-4,0],[2,3]]

S = sum(x for x in nums if x % 2 == 0)

answer = []

for value, index in queries:

    if nums[index] % 2 == 0: 
        S -= nums[index]
    print(S)
    nums[index] += value

    if nums[index] % 2 == 0: 
        S += nums[index]

    print(S)
    answer.append(S)

print(answer)

"""
After adding 1 to nums[0], the array is [2,2,3,4], and the sum of even values is 2 + 2 + 4 = 8.
After adding -3 to nums[1], the array is [2,-1,3,4], and the sum of even values is 2 + 4 = 6.
After adding -4 to nums[0], the array is [-2,-1,3,4], and the sum of even values is -2 + 4 = 2.
After adding 2 to nums[3], the array is [-2,-1,3,6], and the sum of even values is -2 + 6 = 4.
"""
