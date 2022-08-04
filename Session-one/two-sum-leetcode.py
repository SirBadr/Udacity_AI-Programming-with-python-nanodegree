"""
problem statement:
==================
Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.
 
Example 1:
===========
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
==========
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
===========
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
============
2 <= nums.length <= 104
-109 <= nums[i] <= 109
-109 <= target <= 109
Only one valid answer exists.
 

Follow-up: Can you come up with an algorithm that is less than O(n2) time complexity?

"""

# solution one (Prinecton, Mahmoud):
    def twoSumOne(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target and i != j:
                    return [i, j]

# solution two (Nathan):
def twoSumTwo(self, nums, target):
    d = {}
    for i, num in enumerate(nums):
        if target - num in d:
            return [i, d[target-num]]
        d[num] = i


# solution three ( zenret ):
    def twoSumThree(self, nums, target):
        indexs = set()
        for i, num in enumerate(nums):
            diff = target - num

            if diff in nums:
                idx1 = i
                idx2 = nums.index(diff)
                print(idx1)
                print(idx2)
                if idx1 != idx2:
                    indexs.add(idx1)
                    indexs.add(nums.index(diff))

        #if (len(indexs) > 2) or (len(indexs)<=1):
            #print("No solutions found")
        #else:
        #print(indexs)
            
        return indexs