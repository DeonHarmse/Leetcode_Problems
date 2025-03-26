class Solution(object):
    def findDifference(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[List[int]]
        """

        hash1 = {}
        hash2 = {}
        ans1 = []
        ans2 = []

        for iLoop in nums1:
            hash1[iLoop] = True
        
        for iLoop in nums2:
            hash2[iLoop] = True

        for iLoop in hash1.keys():
            if iLoop not in hash2:
                ans1.append(iLoop)

        for iLoop in hash2.keys():
            if iLoop not in hash1:
                ans2.append(iLoop)

        return [ans1, ans2]