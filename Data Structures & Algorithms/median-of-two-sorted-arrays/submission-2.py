class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # 保证 nums1 是短数组
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
        
        m, n = len(nums1), len(nums2)
        total_left = (m + n + 1) // 2
        
        left, right = 0, m
        while left < right:
            mid1 = (left + right) // 2
            mid2 = total_left - mid1
            # 比较 nums1[mid1] 和 nums2[mid2-1]
            if nums1[mid1] < nums2[mid2 - 1]:
                left = mid1 + 1
            else:
                right = mid1
        
        # 循环结束，left 就是切分点
        mid1 = left
        mid2 = total_left - mid1
        
        # 计算左半部分最大值
        if mid1 == 0:
            max_left = nums2[mid2 - 1]
        elif mid2 == 0:
            max_left = nums1[mid1 - 1]
        else:
            max_left = max(nums1[mid1 - 1], nums2[mid2 - 1])
        
        # 如果总长度是奇数，直接返回 max_left
        if (m + n) % 2 == 1:
            return float(max_left)
        
        # 偶数长度，需要右半部分最小值
        # 注意：一定要先检查 mid2 == n，再检查 mid1 == m
        if mid2 == n:
            min_right = nums1[mid1]
        elif mid1 == m:
            min_right = nums2[mid2]
        else:
            min_right = min(nums1[mid1], nums2[mid2])
        
        return (max_left + min_right) / 2.0