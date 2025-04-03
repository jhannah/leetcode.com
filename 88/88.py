# https://leetcode.com/problems/merge-sorted-array/description/?envType=study-plan-v2&envId=top-interview-150
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        del nums1[m:]
        nums1.extend(nums2)
        nums1.sort()


s = Solution()

nums1 = [1,2,3,0,0,0]
s.merge(nums1, 3, [2,5,6], 3)
assert nums1 == [1,2,2,3,5,6]

nums1 = [1]
s.merge(nums1, 1, [], 0)
assert nums1 == [1]

nums1 = [0]
s.merge(nums1, 0, [1], 1)
assert nums1 == [1]

print("PASS", __file__)
