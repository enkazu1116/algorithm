package main

import (
	"fmt"
	"slices"
)

func main() {
	input := []int{4, 1, 5}

	output := false
	output = hasConsecutiveNumbers(input)
	fmt.Printf("回答は: %t", output)
}

func hasConsecutiveNumbers(nums []int) bool {
	slices.Sort(nums)

	for i := 0; i < len(nums)-1; i++ {
		if nums[i]+1 == nums[i+1] {
			return true
		}
	}

	return false
}
