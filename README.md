# Data Structures & Algorithms

The purpose of this repo is to track my progress as I learn Data Structures & Algorithms using Python.

I will be working through this [coding interview study plan](https://www.techinterviewhandbook.org/coding-interview-study-plan/).

Although this is mainly interview prep, I'll be using it as an opportunity to develop my DS&A skills.

## WEEK 1

### Arrays

Arrays hold values of the same type at contiguous memory locations.

In Python we typically know this as a `List` but you can also use do something like:

```python
balance = array.array('i', [300, 200, 100])
```

With 'i' being the data type, and the [300, 200, 100] being the elements of the array.

They are among the most common data structures.

The advantage of an Array is that you can store multiple elements under one single variable name. You can also quickly access elements (assuming you know the index).

The disadvantage of an Array is that it can be slow to remove element or add them to the middle of an array, because remaining elements need to be shifted to accommodate the new or missing element.

In an array, each element has an index which is used to access the element.

```python
# access element
balance[1]

# insert an element
balance.insert(index, 2)

# delete an element
balance.remove(2)

# search an array
balance.index(150)

# update an array
balance[2] = 1

# traverse array
for x in balance:
    print(x)
```

For arrays, reading and writing elements is constant time. Adding or removing from the end is constant.

However, removing the first element means we have to move all the values down in memory. This is O of N. This is true for adding to the beginning, as well as adding or removing from the middle.

Simple arithmetic is used to know where we're going in the array.

Searching an array is log of N.

#### Leetcode Problems

TWO SUM

```python
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
```

BEST TIME TO BUY AND SELL STOCK

```python
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        minimum = float("inf")
        maximum = 0
        for i in range(len(prices)):
            if prices[i] < minimum:
                minimum = prices[i]
            elif prices[i] - minimum > maximum:
                maximum = prices[i] - minimum
            print(maximum)
        return maximum
```

PRODUCT OF ARRAY EXCEPT SELF

```python
class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix = [1]*len(nums)
        count = 1
        for i in range(len(nums)):
            prefix[i] = count
            count *= nums[i]

        postfix = [1]*len(nums)
        count = 1
        for i in range(len(nums) - 1, -1, -1):
            postfix[i] = count
            count *= nums[i]

        answer = []
        for k, v in zip(prefix, postfix):
            answer.append(k * v)

        return answer
```

MAXIMUM SUBARRAY

```python
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        current = nums[0]
        maximum = nums[0]

        for num in nums[1:]:
            if num > current + num:
                current = num
            else:
                current += num

            if current > maximum:
                maximum = current

        return maximum
```

### Strings

Strings are a sequence of characters. May tips that apply to arrays will also apply to strings. Time complexity will also be similar.

Access = O of 1
Search = O of n
Insert = O of n
Remove = O of n

VALID ANAGRAM

```python
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict1 = {}
        dict2 = {}

        for i in s:
            if i in dict1:
                dict1[i] += 1
            else:
                dict1[i] = 1

        for i in t:
            if i in dict2:
                dict2[i] += 1
            else:
                dict2[i] = 1

        if dict1 == dict2:
            return True
        else:
            return False
```

VALID PALINDROME

```python
class Solution:
    def isPalindrome(self, s: str) -> bool:
        valid = "abcdefghijklmnopqrstuvwxyz0123456789"
        new = ""
        for char in s:
            char = char.lower()
            if char in valid:
                new += char

        if new == new[::-1]:
            return True
        else:
            return False
```

LONGEST SUBSTRING WITHOUT REPEATING CHARACTERS

```python
charSet = set()
l = 0
res = 0

for r in range(len(s)):
    while s[r] in charSet:
        charSet.remove(s[l])
        l += 1
    charSet.add(s[r])
    res = max(res, r - l + 1)
return res
```
