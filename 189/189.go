package _189test

func rotateArray(k int, nums []int) []int {
	length := len(nums)
	start := length - k
	end := start + length

	// Regarding ... see "variadic functions"
	//   https://go.dev/doc/go1.17_spec#Passing_arguments_to_..._parameters
	//   https://gobyexample.com/variadic-functions
	nums2 := append(nums, nums...)

	return nums2[start:end]
}
