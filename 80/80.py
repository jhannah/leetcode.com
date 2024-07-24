# 80. Remove Duplicates from Sorted Array II
# https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/solutions/4804983/beats-100-0ms-advanced-two-pointer-approach-java-c-python-rust

class Solution:
  def removeDuplicates(self, nums: list[int]) -> int:
    j = 1
    for i in range(1, len(nums)):
      if j == 1 or nums[i] != nums[j - 2]:
        nums[j] = nums[i]
        j += 1
    return j


s = Solution()
nums = [1, 1, 1, 2, 2, 3]
assert s.removeDuplicates(nums) == 5
assert nums[0:5] == [1, 1, 2, 2, 3]  # stop-1 lol sigh

nums = [0, 0, 1, 1, 1, 1, 2, 3, 3]
assert s.removeDuplicates(nums) == 7
assert nums[0:7] == [0, 0, 1, 1, 2, 3, 3]

print("PASS", __file__)
