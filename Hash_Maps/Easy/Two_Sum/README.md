# Two_Sum

 This program is code to an answer in Leetcode, called Two Sum.
 link: https://leetcode.com/problems/two-sum/
 Problem from leetcode:


-----

Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.

 Example 1:

Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation - Because nums[0] + nums[1] == 9, we return [0, 1].

-----

Definitions and Examples:
Big O -     Big O notation describes the upper bound of an algorithm's runtime or space requirements.
            It focuses on how the algorithm's performance changes as the input size (often denoted as "n") increases.
            Often used to evaluate algorithms such as searching for a variable in an array.
            Big O describes the LONGEST possible time or worst case scenario of the algorithm.
            An example is A = [1, 7, 6, 2, 8]
            Assume the algorithm is:

Enumerate - enumerate() is a built-in Python function that adds a counter to an iterable (list, tuple, string) and returns an enumerate object. This object yields pairs of (index, value) for each element in the iterable. It essentially allows you to iterate through a sequence while keeping track of the index of each element. 

        #Note: you are returning the index at which the number you are looking for is at.

            num2find = 8

            max = len(A)
            for i in range(max):
                if A[i] == num2find:
                    result = i
                    print(f"Number found at index: {result}")


        In this algorithm, the worst case scenario to find the number 8 using this algorithm as it is the last index in the array.
        This means it loops 5 times as the length of the array is 5, or length of n of the array!
        Hence the big O of this algorithm is O(n) (a linear time)




A simple way to do this is to use a "brute force" method.
Checking for every value of the given list(nums) against every other element in the list, summing them to see if it is the target.
This has a big O notation of O(n^2). However, this can be improved via hashmaps!

This uses hashmaps (or rather dictionaries, that are hashed from my understanding).
Hashmaps have a big O for searching as O(1)
This allows us to create a program that can basically 'know' if something exists in the hashmap.
With the code, it only runs through the list once! (n times, hence big O of n)

You loop through the list, checking if the complimentry (target - current value in list), exists in the hashmap.
If it doesn't, add it to the hashmap. Note that this will not work if a hashmap is replaced by a list,
as you would need to perform a linear search (O(n)) through the list to find the complementary number.


Things learned:
-Big O
-enumerate function
-hashmaps