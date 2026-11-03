package main

import "fmt"

// Input: s = "anagram", t = "nagaram"
// Output: true
func valid_anagram(s string, t string) bool {
	if len(s) != len(t) {
		return false
	}

	// 英小文字 a-z の出現回数を添字 0-25 に記録する。
	var counts [26]int

	for i := 0; i < len(s); i++ {
		counts[s[i]-'a']++
		counts[t[i]-'a']--
	}

	for _, count := range counts {
		if count != 0 {
			return false
		}
	}
	return true
}

func main() {
	s := "anagram"
	t := "nagaram"
	fmt.Println(valid_anagram(s, t))
}
