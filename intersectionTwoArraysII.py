class Solution(object):
    def intersect(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
  
        common=[]
        for i in nums1:
            if i in nums2:
                common.append(i)
                nums2.remove(i)
            if len(nums2) == 0:
                return common
        return common
