class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        first, second = m-1, n-1
        k = m+n-1

        while first >= 0 and second >= 0:
            if nums1[first] > nums2[second]:
                nums1[k] = nums1[first]
                first -= 1
            else:

                nums1[k] = nums2[second]
                second -= 1
            k -= 1

        while second >= 0:
            nums1[k] = nums2[second]
            second -= 1
            k -= 1