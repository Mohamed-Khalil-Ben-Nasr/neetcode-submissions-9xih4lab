class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        total = len(nums1) + len(nums2)
        a, b = nums1, nums2
        # we work with min(n,m) because if we work with the max, we risk having
        # a longer range of k and we would risk half - k going negative 
        if len(b) < len(a):
            a, b = b, a
        half = total // 2
        # this is inclusive of len(a) because we can take up len(a) elements from a
        l, r = 0, len(a)
        while l <= r:
            # number of elements we are gonna take from A and add to left half
            k = (l + r) // 2
            # number of elements we are gonna take from B and add to left half
            j = half - k
            # this becomes negative if we dont take a single element from A or B to left half
            aLeft = a[k-1] if (k-1) >= 0 else float("-inf")
            bLeft = b[j-1] if (j-1) >= 0 else float("-inf")
            # this exceeds array length if we take all elements from A or B to left half
            # and there are no more elements to put in right half
            aRight = a[k] if k < len(a) else float("inf")
            bRight = b[j] if j < len(b) else float("inf")

            # this is a valid partition
            if aLeft <= bRight and bLeft <= aRight:
                # odd
                if total % 2:
                    return min(aRight, bRight)
                # even
                else:
                    return (max(aLeft, bLeft) + min(aRight, bRight)) / 2
            # we took too many elements from a
            elif aLeft > bRight:
                r = k - 1
            # we took too many elements from b
            else:
                l = k + 1
                






            

        