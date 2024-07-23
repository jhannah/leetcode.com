// 80. Remove Duplicates from Sorted Array II
// https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/?envType=study-plan-v2&envId=top-interview-150

package _80test

func removeDuplicates(nums []int) (int, []int) {

	index := 1
	occurance := 1

	for i := 1; i < len(nums); i++ {
		if nums[i] == nums[i-1] {
			occurance++
		} else {
			occurance = 1
		}

		if occurance <= 2 {
			nums[index] = nums[i]
			index++
		}
	}

	return index, nums[0:index]
}
