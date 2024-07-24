package _189test

func rotateArray(k int, nums []int) []int {
	length := len(nums)
	start := length - k
	end := start + length
	nums2 := append(nums, nums...)
	return nums2[start:end]
}
