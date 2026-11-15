package main

import (
	"fmt"
	"math"
)

/**
* Note
* 1. 隣の数値を比較する
* 2. 差の絶対値をキー、出現回数をバリューとしたセットを用意する
**/

func main() {
	input := [5]int32{1, 5, 2, 3, 6}

	output := maxiumFrequencyDifference(input)
	fmt.Printf("回答: %d\n", output)
}

// 隣り合う数値の差の絶対値が最も多く出現している回数を取得する
func maxiumFrequencyDifference(nums [5]int32) int32 {
	// HashSetを用意
	set := make(map[int]int)

	count := 0

	maxCount := 0
	// 差を求め、セットにプッシュ
	for i := 0; i < len(nums)-1; i++ {

		remainder := math.Abs(float64(nums[i] - nums[i+1]))

		// keyが存在する場合は、カウントを増やす
		if _, ok := set[int(remainder)]; ok {
			count := set[int(remainder)]
			set[int(remainder)] = count + 1
		} else {
			set[int(remainder)] = count + 1
		}

		if maxCount < set[int(remainder)] {
			maxCount = set[int(remainder)]
		}
	}

	return int32(maxCount)
}
