package main

import (
	"fmt"
	"math/rand"
	"time"
)

func BubbleSort(array []int) []int {
	start_time := time.Now()
	for i := 0; i < len(array)-1; i++ {
		for j := 0; j < len(array)-i-1; j++ {
			if array[j] > array[j+1] {
				array[j], array[j+1] = array[j+1], array[j]
				end_time := time.Now()
				elapsed := end_time.Sub(start_time)
				//fmt.Println(elapsed.Seconds(), array)
				fmt.Println(array)
				fmt.Println(elapsed)
			}

		}
	}
	return array
}

func BubbleSort2(array2 []int) []int {
	start_time := time.Now()
	for i := 0; i < len(array2)-1; i++ {
		for j := 0; j < len(array2)-i-1; j++ {
			if array2[j] > array2[j+1] {
				array2[j], array2[j+1] = array2[j+1], array2[j]
				end_time := time.Now()
				elapsed := end_time.Sub(start_time)
				//fmt.Println(elapsed.Seconds(), array)
				fmt.Println(array2)
				fmt.Print(elapsed)
			}

		}
	}
	return array2
}

func init() {
	rand.Seed(time.Now().UnixNano())
}

func RangeInt(min int, max int, n int) []int {
	arr := make([]int, n)
	var r int
	for r = 0; r <= n-1; r++ {
		arr[r] = rand.Intn(max) + min
	}
	return arr
}

func main() {
	rand.Seed(time.Now().UnixNano())
	array := RangeInt(0, 5000, 10)
	//array := []int{54, 26, 93, 17, 77, 31, 44, 55, 20}
	rand.Shuffle(len(array), func(i, j int) { array[i], array[j] = array[j], array[i] })
	fmt.Println("bubbleSort time:", BubbleSort(array))
	println("-----------------------------------------------------------------------------------------")
	println("Reverse List")
	array2 := RangeInt(5000, 1, 10)
	rand.Shuffle(len(array2), func(i, j int) { array[i], array[j] = array[j], array[i] })
	fmt.Println("bubbleSort time:", BubbleSort2(array))
}
