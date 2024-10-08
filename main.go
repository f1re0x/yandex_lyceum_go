package main

import (
	"fmt"
)

func containsduplicate(nums []int) bool {
	m := make(map[int]bool)
	for _, num := range nums {
		if _, ok := m[num]; ok {
			return true
		}
		m[num] = true
	}
	return false
}

func main() {
	numbers := []int{1, 2, 3, 4, 5, 6, 7, 1, 2, 3}
	fmt.Println(containsduplicate(numbers))
}
