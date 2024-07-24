class Solution:
  def rotateArray(self, k: int, nums: list[int]) -> list[int]:
    length = len(nums)
    start = length - k
    end = start + length
    nums = nums + nums
    return nums[start:end]


s = Solution()
assert s.rotateArray(3, [1, 2, 3, 4, 5, 6, 7]) == [5, 6, 7, 1, 2, 3, 4]
assert s.rotateArray(2, [-1, -100, 3, 99]) == [3, 99, -1, -100]

print("Python: success")
