# Difference of Two Arrays

 This program is code to an answer in Leetcode, called Two Sum.
 link: https://leetcode.com/problems/find-the-difference-of-two-arrays/description/?envType=study-plan-v2&envId=leetcode-75
 Problem from leetcode:

My solution loops through each array and creates a dictionary (or rather, hashmap), which stores all values of the array.
The hashmap allows us to search with a time complexity of O(1).
Hence, we check to see if a value exists in our respective hashmaps, if it does not exist (is distinct), then append it to our respective answer list.
This solution is good, but has a flaw, if there are multiple values in a list, we are redundantly overwriding the values in the hashmap.
This can be avoided by using Pythons set() function, which creates a dictionary with unique values, without redundancy.
An example of this code is below:

Python

class Solution(object):
    def findDifference(self, nums1, nums2):
        hash1 = set(nums1)  # Use sets directly from the start
        hash2 = set(nums2)
        ans1 = []
        ans2 = []

        for num in hash1:
            if num not in hash2:
                ans1.append(num)

        for num in hash2:
            if num not in hash1:
                ans2.append(num)

        return [ans1, ans2]


What I learned:
- set() function