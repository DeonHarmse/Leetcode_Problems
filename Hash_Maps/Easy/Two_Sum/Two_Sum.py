class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        hashmap= {}  #technically a dictionary, but has underlying hash mechanincs in the code
        for index, value in enumerate(nums):  #enumerated splits the list into the index and it's value in a list
            complement = target - value  #the value you need to sum to the current index to make the target, called complement
            if complement in hashmap:  
                return [index, hashmap[complement]]  #returns the indexes, which when their values are added, makes the target num
            hashmap[value]= index  