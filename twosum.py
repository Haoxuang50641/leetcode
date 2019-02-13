class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        target_rec = 0
        result = []
        for k in range(len(nums)):
            if target > 0:
                if nums[k] < target:
                    target_rec = target - nums[k]

                for len2 in range(len(nums)):
                    if len2 != k:    
                        if nums[len2] == target_rec:
                            result.append(k)
                            result.append(len2)
                if len(result) == 2:
                    break
            elif target == 0:
                for len2 in range(len(nums)):
                    if len2 != k and nums[len2] + nums[k] == 0:
                            result.append(k)
                            result.append(len2)
                if len(result) == 2:
                    break
            else:
                target_rec = target - nums[k]

                for len2 in range(len(nums)):
                    if len2 != k:    
                        if nums[len2] == target_rec:
                            result.append(k)
                            result.append(len2)
                if len(result) == 2:
                    break
        return result